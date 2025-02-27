def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    nums = sorted(lst[10:67])
    if len(nums) < 2:
        return None
    return nums[1]