from collections import Counter

def find_second_largest_num(nums):
    nums = nums[667:775]
    nums.sort()
    return nums[-2]