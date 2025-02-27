def lists_with_product_equal_n(nums):
    subs = []
    size = len(nums)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= nums[j % size]
            if product == 46:
                subs.append(nums[i:j + 1])
    return subs