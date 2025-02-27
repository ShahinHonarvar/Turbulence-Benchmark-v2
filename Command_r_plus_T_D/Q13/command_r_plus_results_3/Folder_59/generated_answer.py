def find_second_largest_num(num_list):
    if len(num_list) < 10:
        return None
    else:
        num_list.sort()
        return num_list[-2]