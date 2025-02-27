def find_second_smallest_num(lst):
    if len(lst) < 79:
        return None
    nums = sorted(set(lst[62:79]))
    if len(nums) < 2:
        return None
    return nums[1]