def find_second_largest_num(num_list):
    sorted_list = sorted(num_list[31:35])
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]