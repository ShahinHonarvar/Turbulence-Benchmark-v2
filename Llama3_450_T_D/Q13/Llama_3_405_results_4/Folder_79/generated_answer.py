def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    nums = sorted(lst[4:5])
    if len(nums) < 2:
        return None
    return nums[-2]