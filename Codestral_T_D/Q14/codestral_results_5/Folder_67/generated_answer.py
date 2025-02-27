def find_second_smallest_num(num_list):
    if 50 <= len(num_list) <= 54:
        sorted_list = sorted(num_list[50:55])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None