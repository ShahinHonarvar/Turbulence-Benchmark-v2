def find_second_largest_num(num_list):
    num_list.sort()
    if len(num_list) >= 8:
        return num_list[-2]
    else:
        return None