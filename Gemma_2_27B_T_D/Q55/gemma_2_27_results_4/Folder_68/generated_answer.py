def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 0 and all((x != 0 for x in sublist)) and (prod(sublist) == 6):
                result.append(sublist)
    return result

def prod(nums):
    p = 1
    for x in nums:
        p *= x
    return p