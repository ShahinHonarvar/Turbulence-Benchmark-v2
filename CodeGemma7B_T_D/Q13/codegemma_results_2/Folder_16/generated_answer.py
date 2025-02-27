def find_second_largest_num(num_list):
    new_list = sorted(num_list[33:37])
    if len(new_list) < 2:
        return None
    else:
        return new_list[-2]