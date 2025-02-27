def find_second_largest_num(num_list):
    if len(num_list) < 101:
        return None
    num_list.sort()
    return num_list[-2]