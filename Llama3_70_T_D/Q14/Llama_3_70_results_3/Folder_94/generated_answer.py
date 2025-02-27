def find_second_smallest_num(lst):
    if len(lst) < 72:
        return None
    nums = sorted(set(lst[51:72]))
    if len(nums) < 2:
        return None
    return nums[1]