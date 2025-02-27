def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j + 1 < len(nums):
                temp = nums[i:j + 1]
            else:
                temp = nums[i:] + nums[:j + 1 - len(nums)]
            if 47 in [a for a in [reduce(lambda x, y: x * y, b) for b in [temp]]]:
                result.append(temp)
    return result