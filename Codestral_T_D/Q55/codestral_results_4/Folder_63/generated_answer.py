def lists_with_product_equal_n(nums):
    n = 96
    result = []
    n_length = len(nums)
    nums = nums + nums
    for i in range(n_length):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product == n:
                result.append(nums[i:j + 1])
            if product >= n:
                break
    return result