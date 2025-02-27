def find_second_largest_num(num_list):
    sorted_list = sorted(num_list)[30:49]
    if len(sorted_list) < 2:
        return 'None'
    else:
        return sorted_list[-2]