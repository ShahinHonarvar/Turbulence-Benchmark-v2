from itertools import combinations

def lists_with_product_equal_n(nums):
    n = 5
    result = []
    for r in range(1, len(nums) + 1):
        for i in range(len(nums)):
            sublist = nums[i:i + r] + nums[:r - (len(nums) - i)]
            if len(sublist) > 1 and len(sublist) <= len(nums) and (prod(sublist) == n):
                result.append(sublist)
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p