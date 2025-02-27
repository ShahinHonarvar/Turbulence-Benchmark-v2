def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) >= 24 and num_list[23] != num_list[24]:
        return num_list[24]
    else:
        return 'None'