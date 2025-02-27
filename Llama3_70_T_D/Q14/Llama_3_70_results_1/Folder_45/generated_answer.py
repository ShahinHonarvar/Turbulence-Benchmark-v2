def find_second_smallest_num(num_list):
    num_list = num_list[30:201]
    if len(num_list) < 2:
        return None
    return sorted(set(num_list))[1]