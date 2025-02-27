def find_largest_num(num_list):
    if len(num_list) < 89:
        return None
    return max(num_list[21:89])