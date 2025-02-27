def find_second_largest_num(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return None
    max_num = max(lst[686:988])
    second_max_num = None
    for num in lst[686:988]:
        if num != max_num:
            if second_max_num is None or num > second_max_num:
                second_max_num = num
    return second_max_num