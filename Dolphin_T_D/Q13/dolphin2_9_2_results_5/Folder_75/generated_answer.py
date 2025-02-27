def find_second_largest_num(lst):
    sub_lst = lst[56:58]
    if len(sub_lst) < 2:
        return None
    first = second = float('-inf')
    for x in sub_lst:
        if x > first:
            first, second = (x, first)
        elif x < first and x > second:
            second = x
    if second == float('-inf'):
        return None
    return second