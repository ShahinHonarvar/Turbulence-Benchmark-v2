def lists_with_product_equal_n(nums):
    results = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product == -15:
                results.append(nums[i:j + 1])
            elif product > -15:
                break
    return results