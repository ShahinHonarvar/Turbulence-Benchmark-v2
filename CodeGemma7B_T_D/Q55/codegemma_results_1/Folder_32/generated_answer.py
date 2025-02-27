def lists_with_product_equal_n(nums):
    for i in range(len(nums)):
        product = nums[i]
        j = i + 1
        while j % len(nums) != i:
            if product == 76:
                return [[nums[i:j]]]
            product *= nums[j]
            j += 1
    return []