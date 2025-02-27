def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 26 or max(num_list) - min(num_list) < 26:
        return 'None'
    num_list.sort()
    return num_list[15]