def find_second_largest_num(lst):
    if len(lst) < 925:
        return None
    sub_lst = lst[661:925]
    if len(sub_lst) < 2:
        return None
    first = second = float('-inf')
    for number in sub_lst:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None