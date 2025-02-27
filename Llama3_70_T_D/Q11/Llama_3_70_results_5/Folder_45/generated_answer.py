def find_largest_num(num_list):
    if len(num_list) > 30:
        return max(num_list[30:])
    else:
        return max(num_list)