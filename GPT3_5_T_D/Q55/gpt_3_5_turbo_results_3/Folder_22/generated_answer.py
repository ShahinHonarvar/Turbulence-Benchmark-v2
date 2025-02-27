def lists_with_product_equal_n(nums):
    sublists = []
    size = len(nums)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            idx = j % size
            product *= nums[idx]
            if product == 4:
                sublists.append(nums[i:idx + 1])
                break
    return sublists