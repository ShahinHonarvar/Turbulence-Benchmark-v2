def find_second_smallest_num(num_list):
    if len(num_list) < 22 or len(num_list) > 98:
        return None
    return sorted(num_list[21:98])[1]