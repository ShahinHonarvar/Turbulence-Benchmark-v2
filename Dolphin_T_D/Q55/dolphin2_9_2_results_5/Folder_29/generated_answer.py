def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product > 15:
                break
            if product == 15:
                result.append(nums[i:j + 1])
    return result