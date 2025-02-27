def find_second_smallest_num(num_list):
    if len(num_list) < 51:
        return None
    sub_list = num_list[43:52]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[1]