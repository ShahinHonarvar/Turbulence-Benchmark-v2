def find_second_largest_num(lst):
    sublist = lst[82:87]
    if len(sublist) == 0:
        return None
    max_num = sublist[0]
    second_max_num = None
    for num in sublist[1:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num != max_num and (second_max_num is None or second_max_num < num):
            second_max_num = num
    return second_max_num