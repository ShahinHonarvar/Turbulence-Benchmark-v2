def find_second_largest_num(lst):
    if not lst or len(lst) < 2:
        return None
    sub_lst = lst[75:89]
    if len(sub_lst) < 2:
        return None
    first, second = (None, None)
    for num in sub_lst:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second