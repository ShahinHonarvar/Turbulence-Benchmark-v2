def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    lst = lst[246:750]
    if len(lst) < 2:
        return None
    first = max(lst)
    second = 0
    for num in lst:
        if num != first and (second == 0 or num > second):
            second = num
    if second != 0:
        return second
    else:
        return None