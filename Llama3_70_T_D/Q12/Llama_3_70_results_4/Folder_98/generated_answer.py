def find_smallest_num(num_list):
    if len(num_list) > 5:
        return min(num_list[:6])
    else:
        return min(num_list)