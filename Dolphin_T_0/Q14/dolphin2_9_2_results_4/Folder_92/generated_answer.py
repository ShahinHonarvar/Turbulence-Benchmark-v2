def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min_num = min(lst[0], lst[1])
    second_min_num = max(lst[0], lst[1])
    for num in lst[2:]:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif num < second_min_num:
            second_min_num = num
    if min_num == second_min_num:
        return None
    else:
        return second_min_num