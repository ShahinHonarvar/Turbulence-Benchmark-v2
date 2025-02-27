def find_second_smallest_num(num_list):
    if 33 <= len(num_list) <= 36:
        sorted_num_list = sorted(num_list[33:37])
        return sorted_num_list[1] if len(sorted_num_list) > 1 else None
    else:
        return None