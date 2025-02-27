def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    nums_from_23 = sorted(nums[23:])
    if len(nums_from_23) < 2:
        return None
    return nums_from_23[1]