def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 27 or max(num_list) == min(num_list):
        return None
    num_list = sorted(num_list[26:53])
    return num_list[-2]