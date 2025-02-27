def find_second_smallest_num(l_numbers):
    sub_list = l_numbers[56:67]
    if len(sub_list) < 2:
        return None
    min_1 = min(sub_list)
    sub_list.remove(min_1)
    if len(sub_list) < 2:
        return None
    min_2 = min(sub_list)
    return min_2