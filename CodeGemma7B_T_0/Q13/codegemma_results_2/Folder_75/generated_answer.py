def find_second_largest_num(num_list):
    if len(num_list) < 58 or not num_list[56:58]:
        return 'None'
    return sorted(num_list[56:58])[-2]