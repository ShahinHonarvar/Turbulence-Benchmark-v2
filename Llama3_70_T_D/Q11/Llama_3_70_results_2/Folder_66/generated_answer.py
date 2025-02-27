def find_largest_num(num_list):
    if len(num_list) < 55:
        return max(num_list)
    else:
        return max(num_list[50:55])