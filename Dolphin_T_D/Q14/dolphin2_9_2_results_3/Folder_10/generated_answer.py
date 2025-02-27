def find_second_smallest_num(num_list):
    if 62 <= len(num_list) <= 92:
        sorted_list = sorted(num_list[62:93])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None