def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 67:
        return 'None'
    num_list = sorted(num_list[10:67])
    return num_list[1]