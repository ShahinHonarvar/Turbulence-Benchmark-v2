def find_second_largest_num(num_list):
    if len(num_list) < 2 or len(num_list) > 9:
        return None
    sorted_list = sorted(num_list[:9])
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]