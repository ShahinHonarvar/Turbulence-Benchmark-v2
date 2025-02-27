def lists_with_product_equal_n(nums):
    n = 54
    size = len(nums)
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= nums[j % size]
            if product == n:
                result.append(nums[i:j % size + 1])
            elif product > n:
                break
    return result