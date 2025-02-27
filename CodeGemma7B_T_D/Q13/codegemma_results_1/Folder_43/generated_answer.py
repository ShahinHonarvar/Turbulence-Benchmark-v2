def find_second_largest_num(num_list):
    num_list_range = num_list[68:87]
    num_list_range.sort()
    if len(num_list_range) > 1:
        return num_list_range[-2]
    else:
        return 'None'