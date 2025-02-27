def find_second_smallest_num(num_list):
    if len(num_list) < 74 or len(num_list) > 95:
        return 'None'
    return sorted(num_list[74:96])[1]