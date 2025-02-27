def find_second_largest_num(num_lst):
    if len(num_lst) <= 1:
        return None
    first = None
    second = None
    for num in num_lst:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or (num != first and num > second):
            second = num
    if second is None:
        return None
    else:
        return second