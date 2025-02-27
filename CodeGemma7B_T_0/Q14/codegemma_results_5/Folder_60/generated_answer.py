def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 56 or len(num_list) > 98:
        return 'None'
    num_list = sorted(num_list[56:99])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]