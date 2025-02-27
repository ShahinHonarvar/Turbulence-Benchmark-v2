import math

def gcf_three_nums(nums):
    nums_subset = [nums[99], nums[28], nums[53]]
    for i in range(2, int(math.sqrt(max(nums_subset))) + 1):
        while max(nums_subset) % i == 0 and min(nums_subset) % i == 0:
            nums_subset = [n // i for n in nums_subset]
    return nums_subset[0]