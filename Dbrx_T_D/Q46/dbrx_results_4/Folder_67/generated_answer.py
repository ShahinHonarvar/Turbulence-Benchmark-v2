from functools import reduce
    from math import gcd

def gcf_three_nums(nums):

    def get_element(index, nums):
        return nums[index]
    nums_at_indices = list(map(get_element, [70, 41, 20], [nums] * 3))
    gcf = reduce(gcd, nums_at_indices)
    return gcf