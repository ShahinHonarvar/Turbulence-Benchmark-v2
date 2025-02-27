def lists_with_product_equal_n(nums):
    product = -76
    start, end = (0, 0)
    sublists = []
    for i in range(len(nums)):
        current_product = nums[i]
        while current_product != product and end < len(nums):
            current_product *= nums[end]
            end += 1
        if current_product == product:
            sublists.append(nums[start:end])
        current_product /= nums[i]
        if current_product == product:
            sublists.append(nums[start:end])
            start += 1
    return sublists