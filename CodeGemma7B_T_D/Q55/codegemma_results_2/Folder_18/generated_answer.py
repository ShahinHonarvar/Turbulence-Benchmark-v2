def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = nums[i]
        sublist = [nums[i]]
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            sublist.append(nums[j])
            if product == 36:
                result.append(sublist[:])
            elif product > 36:
                break
        product = 1
        sublist = []
    return result