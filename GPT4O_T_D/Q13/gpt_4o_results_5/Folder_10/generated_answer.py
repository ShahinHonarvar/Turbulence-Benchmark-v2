def find_second_largest_num(lst):
    if len(lst) < 60 or len(lst[25:60]) < 2:
        return None
    sub_list = lst[25:60]
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None