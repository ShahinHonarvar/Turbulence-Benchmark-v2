def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    nums = sorted(lst[29:52])
    if len(nums) < 2:
        return None
    return nums[1]