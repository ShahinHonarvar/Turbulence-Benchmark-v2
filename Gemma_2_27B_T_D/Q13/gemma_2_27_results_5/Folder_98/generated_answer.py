def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums_sorted = sorted(nums[0:7])
    return nums_sorted[-2]