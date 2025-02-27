def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[70:85])
    second_max_num = None
    for i in range(14):
        if lst[i] != max_num and (second_max_num is None or second_max_num < lst[i]):
            second_max_num = lst[i]
    return second_max_num if second_max_num != None else None