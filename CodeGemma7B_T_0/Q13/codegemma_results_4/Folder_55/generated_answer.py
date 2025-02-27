def find_second_largest_num(num_list):
    if len(num_list) < 2 or max(num_list) == num_list[-1]:
        return None
    return sorted(num_list)[-2]