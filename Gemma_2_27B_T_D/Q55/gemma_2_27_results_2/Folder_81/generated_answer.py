def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if len(nums[i:j]) == 1 and nums[i] != 8:
                continue
            product = 1
            for k in range(i, j):
                product *= nums[k % len(nums)]
            if product == -8:
                result.append(nums[i:j])
    return result