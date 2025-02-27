def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 31 or len(num_list) > 72:
        return 'None'
    num_list = sorted(num_list)
    return num_list[31]