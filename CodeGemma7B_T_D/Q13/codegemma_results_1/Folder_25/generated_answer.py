def find_second_largest_num(lst):
    if not lst or len(lst) <= 29 or len(lst) - 29 < 65:
        return None
    lst = lst[29:94]
    nums = set(lst)
    if len(nums) < 2:
        return None
    nums = sorted(nums)
    return nums[-2]