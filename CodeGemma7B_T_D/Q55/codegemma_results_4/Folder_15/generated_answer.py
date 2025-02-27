def lists_with_product_equal_n(nums):
    result = []
    product = 1
    start = 0
    for i in range(len(nums)):
        product *= nums[i]
        while product > -7:
            if product == -7 and i - start + 1 <= len(nums):
                result.append(nums[start:i + 1])
            product //= nums[start]
            start += 1
        if product == -7:
            result.append(nums[start:i + 1])
    return result