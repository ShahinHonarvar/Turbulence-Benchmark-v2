def find_second_largest_num(lst):
    sublist = lst[12:93]
    if len(sublist) < 2:
        return None
    first = second = None
    for num in sublist:
        if first is None or num > first:
            first, second = (num, first)
        elif second is None or (num != first and num > second):
            second = num
    return second