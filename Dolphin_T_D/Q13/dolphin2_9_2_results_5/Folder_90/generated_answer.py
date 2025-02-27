def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = None
    second_max_num = None
    for number in lst[262:747]:
        if max_num is None or number > max_num:
            second_max_num = max_num
            max_num = number
        elif second_max_num is None or (number > second_max_num and number < max_num):
            second_max_num = number
    return second_max_num