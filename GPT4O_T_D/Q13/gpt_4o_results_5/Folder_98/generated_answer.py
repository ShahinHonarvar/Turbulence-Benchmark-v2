def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    subset = lst[:7]
    first, second = (float('-inf'), float('-inf'))
    for num in subset:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None