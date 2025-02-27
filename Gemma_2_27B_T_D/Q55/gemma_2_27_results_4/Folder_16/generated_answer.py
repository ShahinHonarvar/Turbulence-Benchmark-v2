def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if eval('*'.join((str(x) for x in nums[i:j]))) == -837:
                result.append(nums[i:j])
    return result