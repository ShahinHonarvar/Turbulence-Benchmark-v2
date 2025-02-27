def find_second_largest_num(num_list):
    num_list.sort()
    if not num_list[75:95]:
        return 'None'
    else:
        return num_list[93]