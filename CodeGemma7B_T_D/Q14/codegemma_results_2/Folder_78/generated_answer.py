def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 17:
        return 'None'
    sorted_list = sorted(num_list[16:79])
    if len(sorted_list) < 2:
        return 'None'
    return sorted_list[1]