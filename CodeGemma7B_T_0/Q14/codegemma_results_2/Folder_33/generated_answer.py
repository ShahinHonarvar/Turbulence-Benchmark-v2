def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 263 or max(num_list) < 262 or (min(num_list) > 746):
        return None
    num_list = sorted(num_list[262:747])
    return num_list[1]