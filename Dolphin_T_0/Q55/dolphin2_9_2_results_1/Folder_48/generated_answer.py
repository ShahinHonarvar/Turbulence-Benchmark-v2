def lists_with_product_equal_n(nums):
    result = []
    if len(nums) == 0:
        return []
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    product = 1
    for i in range(n):
        prefix[i] = nums[i - 1] * product
        product *= nums[i]
    product = 1
    for i in range(n - 1, -1, -1):
        suffix[i] = nums[i + 1] * product
        product *= nums[i]
    for i in range(n):
        for j in range(i, n):
            if prefix[i] * suffix[j] == 990:
                if i == 0 or j == n - 1:
                    result.append(nums[i:j + 1])
                else:
                    result.append(nums[i:j + 1] + nums[0:i])
                    result.append(nums[j + 1:n] + nums[0:j + 1])
    return result