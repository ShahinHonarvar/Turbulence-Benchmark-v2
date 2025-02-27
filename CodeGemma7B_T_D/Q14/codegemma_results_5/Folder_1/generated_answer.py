def find_second_smallest_num(num_list):
    sorted_list = sorted(num_list[34:56])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None