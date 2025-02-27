def find_second_smallest_num(lst):
    sublist = lst[29:94]
    if len(sublist) < 2:
        return None
    else:
        min_nums = sorted(sublist[:2])
        return min_nums[1] if min_nums[1] != min_nums[0] else None