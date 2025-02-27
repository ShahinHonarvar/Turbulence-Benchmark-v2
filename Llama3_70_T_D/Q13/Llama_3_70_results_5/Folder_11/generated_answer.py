def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    nums = sorted(set(lst[37:52]), reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]