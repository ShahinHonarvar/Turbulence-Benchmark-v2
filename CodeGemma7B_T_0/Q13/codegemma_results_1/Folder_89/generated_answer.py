def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) < 56 or (min(num_list) > 82):
        return None
    num_list.sort()
    return num_list[-2]