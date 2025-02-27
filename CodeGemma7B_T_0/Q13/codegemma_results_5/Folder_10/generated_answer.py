def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 26 or max(num_list[:25]) == max(num_list[25:60]):
        return 'None'
    return sorted(num_list[25:60])[-2]