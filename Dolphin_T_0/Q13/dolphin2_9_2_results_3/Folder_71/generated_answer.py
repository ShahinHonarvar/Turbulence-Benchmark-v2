def find_second_largest_num(data):
    sub_list = data[26:53]
    if len(sub_list) < 2:
        return None
    first, second = (0, 0)
    for num in sub_list:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    if second == 0:
        return None
    return second