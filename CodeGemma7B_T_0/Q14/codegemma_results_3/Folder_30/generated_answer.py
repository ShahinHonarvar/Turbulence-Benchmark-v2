def find_second_smallest_num(num_list):
    if len(num_list) < 27 or max(num_list) < 26 or min(num_list) > 52:
        return 'None'
    num_list = sorted(num_list)[26:53]
    return num_list[1]