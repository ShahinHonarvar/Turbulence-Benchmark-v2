def find_second_smallest_num(num_list):
    if len(num_list) < 5:
        return 'None'
    num_list.sort()
    return num_list[1]