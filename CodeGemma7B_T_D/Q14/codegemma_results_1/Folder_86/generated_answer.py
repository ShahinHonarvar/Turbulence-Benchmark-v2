def find_second_smallest_num(lst):
    if len(lst) < 33 or min(lst) == lst[33]:
        return None
    nums = lst[33:37]
    return sorted(nums)[1]