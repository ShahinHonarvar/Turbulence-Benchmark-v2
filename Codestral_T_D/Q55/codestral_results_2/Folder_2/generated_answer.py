def lists_with_product_equal_n(nums):
    n = -968
    size = len(nums)
    nums = nums + nums
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= nums[end]
            if product == n:
                result.append(nums[start:end + 1])
            if product == 0:
                break
    return result