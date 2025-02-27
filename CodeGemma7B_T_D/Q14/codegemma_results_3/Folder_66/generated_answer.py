def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2 or min(num_list) > 99 or (max(num_list) < 62):
        return 'None'
    num_list = sorted(num_list)
    return num_list[62]