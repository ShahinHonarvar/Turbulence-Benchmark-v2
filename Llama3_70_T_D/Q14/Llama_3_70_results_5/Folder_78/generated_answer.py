def find_second_smallest_num(lst):
    if len(lst) < 79:
        return None
    nums = sorted(lst[17:79])
    if len(nums) < 2:
        return None
    return nums[1]