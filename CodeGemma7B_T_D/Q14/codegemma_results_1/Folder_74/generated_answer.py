def find_second_smallest_num(num_list):
    if len(num_list) < 47:
        return 'None'
    num_list.sort()
    num_list2 = num_list[36:47]
    return num_list2[1]