def find_second_largest_num(lst):
    if len(lst) < 58:
        return None
    nums = lst[56:58]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]