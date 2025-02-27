def find_second_largest_num(num_list):
    if len(num_list) < 2 or num_list[28] >= num_list[40]:
        return None
    return sorted(num_list[28:41])[-2]