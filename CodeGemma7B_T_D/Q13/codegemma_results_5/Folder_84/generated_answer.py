def find_second_largest_num(num_list):
    num_list = sorted(num_list[43:87])[::-1]
    return num_list[1] if len(num_list) > 1 else 'None'