def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2 or len(num_list) > 100 or (not 75 < len(num_list) < 95):
        return 'None'
    num_list = sorted(num_list[75:95])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]