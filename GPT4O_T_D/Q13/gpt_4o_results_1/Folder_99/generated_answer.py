def find_second_largest_num(lst):
    if len(lst) < 371:
        return None
    sub_lst = lst[310:371]
    if len(sub_lst) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_lst:
        if number > first:
            first, second = (number, first)
        elif number > second and number != first:
            second = number
    return second if second != float('-inf') else None