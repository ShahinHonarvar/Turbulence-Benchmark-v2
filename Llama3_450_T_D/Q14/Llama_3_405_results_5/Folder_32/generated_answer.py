def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    nums = sorted(lst[32:36])
    if len(nums) < 2:
        return None
    return nums[1]