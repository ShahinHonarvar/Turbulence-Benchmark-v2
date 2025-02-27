def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    return sorted(num_list)[1]