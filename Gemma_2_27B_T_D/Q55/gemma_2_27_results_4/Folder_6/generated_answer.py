def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subset = nums[i:j]
            if len(subset) > len(nums) // 2:
                break
            product = 1
            for num in subset:
                product *= num
            if product == 42:
                sublists.append(subset)
    return sublists