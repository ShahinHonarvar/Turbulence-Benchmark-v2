def find_second_largest_num(num_list):
    if len(num_list) == 0 or len(num_list) < 976:
        return None
    else:
        return sorted(num_list[639:976])[-2]