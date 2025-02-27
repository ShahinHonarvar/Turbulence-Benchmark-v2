def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    s_min1, s_min2 = (lst[0], lst[1])
    if s_min1 > s_min2:
        s_min1, s_min2 = (s_min2, s_min1)
    for num in lst[2:]:
        if num < s_min1:
            s_min1, s_min2 = (num, s_min1)
        elif s_min1 < num < s_min2:
            s_min2 = num
    return s_min2 if s_min2 != lst[1] else None