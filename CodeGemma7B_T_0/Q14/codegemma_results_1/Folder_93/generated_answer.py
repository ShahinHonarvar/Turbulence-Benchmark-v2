def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 80:
        return 'None'
    num_list = sorted(num_list[75:89])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]