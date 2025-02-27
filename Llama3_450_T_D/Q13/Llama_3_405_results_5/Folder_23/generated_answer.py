def find_second_largest_num(lst):
    if len(lst) < 72:
        return None
    nums = lst[52:72]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]