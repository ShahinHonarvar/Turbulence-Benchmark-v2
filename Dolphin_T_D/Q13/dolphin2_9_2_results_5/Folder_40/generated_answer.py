def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    max_num = max(lst[0], lst[1], lst[2])
    second_max = None
    for num in lst:
        if num != max_num:
            if second_max is None or num > second_max:
                second_max = num
    return second_max