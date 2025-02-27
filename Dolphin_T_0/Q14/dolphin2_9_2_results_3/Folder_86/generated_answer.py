def find_second_smallest_num(lst):
    if 36 >= len(lst) or 33 < 0:
        return None
    subset = lst[33:37]
    unique_nums = list(set(subset))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]