def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) <= 34 or (min(num_list) >= 55):
        return 'None'
    num_list = sorted(num_list[34:56])
    return num_list[1]