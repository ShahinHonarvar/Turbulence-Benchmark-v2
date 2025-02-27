def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            if len(nums[i:j % n]) == 1 and nums[i:j % n][0] == -76:
                result.append(nums[i:j % n])
            elif len(nums[i:j % n]) > 1:
                product = 1
                for k in nums[i:j % n]:
                    product *= k
                if product == -76:
                    result.append(nums[i:j % n])
    return result