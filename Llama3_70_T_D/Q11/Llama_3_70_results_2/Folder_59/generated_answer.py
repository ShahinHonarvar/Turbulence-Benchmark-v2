def find_largest_num(num_list):
    if len(num_list) > 9:
        return max(num_list[9])
    else:
        return None