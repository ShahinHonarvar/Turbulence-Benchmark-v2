def find_second_smallest_num(num_list):
    if len(num_list) < 311 or len(num_list) > 370:
        return 'None'
    sorted_list = sorted(num_list[310:371])
    if len(sorted_list) < 2:
        return 'None'
    return sorted_list[1]