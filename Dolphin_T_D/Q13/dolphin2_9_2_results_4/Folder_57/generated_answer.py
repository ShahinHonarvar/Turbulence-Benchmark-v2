def find_second_largest_num(lst):
    sublist = lst[27:56]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second