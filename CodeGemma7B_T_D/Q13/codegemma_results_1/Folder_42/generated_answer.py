def find_second_largest_num(num_list):
    if len(num_list) > 28:
        num_list = sorted(num_list)[29:80]
        if len(num_list) > 1:
            return num_list[-2]
    return None