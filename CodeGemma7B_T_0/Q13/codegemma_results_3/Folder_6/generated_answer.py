def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 11 or max(num_list) < 10 or (min(num_list) > 66):
        return None
    num_list = sorted(num_list)
    return num_list[-2]