def find_second_largest_num(lst):
    sub_lst = lst[639:976]
    if len(sub_lst) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_lst:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None