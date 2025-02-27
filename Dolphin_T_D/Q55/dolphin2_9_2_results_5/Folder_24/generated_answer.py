def lists_with_product_equal_n(nums):
    result = []
    nums = nums + nums[:len(nums) // 2]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k]
            if product == -89:
                result.append(nums[i:j + 1])
    return result