def find_largest_num(num_list):
    if len(num_list) < 58:
        return None
    else:
        return max(num_list[56:58])