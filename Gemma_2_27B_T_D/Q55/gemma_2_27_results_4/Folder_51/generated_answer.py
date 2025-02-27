def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i > j:
                sublist = nums[j:] + nums[:i]
            else:
                sublist = nums[i:j + 1]
            if product(sublist) == -44:
                result.append(sublist)
    return result

def product(nums):
    p = 1
    for num in nums:
        p *= num
    return p