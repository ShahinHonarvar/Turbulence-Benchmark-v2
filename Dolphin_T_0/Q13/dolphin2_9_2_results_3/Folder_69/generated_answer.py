def find_second_largest_num(num_list):
    if len(num_list[32:36]) < 2:
        return None
    else:
        return sorted(num_list[32:36])[1]