def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j + 1 < len(nums):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
            else:
                product = 1
                for k in range(i, len(nums)):
                    product *= nums[k]
                for k in range(0, j - len(nums) + 1):
                    product *= nums[k]
            if product == 76:
                result.append(nums[i:j + 1])
    return result