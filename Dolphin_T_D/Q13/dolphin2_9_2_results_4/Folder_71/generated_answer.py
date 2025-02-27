def find_second_largest_num(num_list):
    sub_list = num_list[25:52]
    if len(sub_list) < 2:
        second_largest = None
    else:
        max_num = max(sub_list)
        sub_list.remove(max_num)
        if len(sub_list) == 0:
            second_largest = None
        else:
            second_largest = max(sub_list)
    return second_largest