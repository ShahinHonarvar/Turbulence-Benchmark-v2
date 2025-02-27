def find_largest_num(num_list):
    if num_list and len(num_list) >= 7:
        return max(num_list[0:8])
    else:
        return None