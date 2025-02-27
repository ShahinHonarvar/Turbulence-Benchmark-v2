from functools import reduce
import operator

def lists_with_product_equal_n(nums):
    n = 90
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if reduce(operator.mul, sublist, 1) == n:
                result.append(sublist)
        nums.append(nums.pop(0))
    return result