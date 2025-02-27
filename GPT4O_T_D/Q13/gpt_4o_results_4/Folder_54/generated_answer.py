def find_second_largest_num(lst):
    if len(lst) < 56 or len(lst[34:56]) < 2:
        return None
    sublist = lst[34:56]
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return None if second == float('-inf') else second