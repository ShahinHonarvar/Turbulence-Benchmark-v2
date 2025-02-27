def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = nums[i]
        if product == -32:
            result.append([nums[i]])
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            if product == -32:
                result.append(nums[i:j + 1])
            if abs(product) > 32:
                break
    return result