def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if all((nums[k] for k in range(i, j + 1))) and reduce(lambda x, y: x * y, nums[i:j + 1]) == -83:
                result.append(nums[i:j + 1])
    return result