def find_second_smallest_num(num_list):
    if len(num_list) < 2 or max(num_list) <= num_list[0]:
        return None
    return sorted(num_list)[1]