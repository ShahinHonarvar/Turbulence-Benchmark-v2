def find_second_largest_num(numbers_list):
    sub_list = numbers_list[22:89]
    if len(sub_list) == 0:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    if len(sub_list) == 0:
        return None
    second_max_num = max(sub_list)
    return second_max_num