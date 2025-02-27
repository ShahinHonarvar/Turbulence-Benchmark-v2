def find_second_smallest_num(lst):
    if len(lst) < 93:
        return None
    nums = sorted(set(lst[19:93]))
    if len(nums) < 2:
        return None
    return nums[1]