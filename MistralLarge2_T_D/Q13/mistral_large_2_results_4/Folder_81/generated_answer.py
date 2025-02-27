def find_second_largest_num(lst):
    if len(lst) < 101:
        return None
    sub_lst = lst[10:101]
    if len(sub_lst) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_lst:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None