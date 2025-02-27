def find_second_largest_num(lst):
    if len(lst) < 81 or len(lst[40:81]) < 2:
        return None
    sublist = lst[40:81]
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None