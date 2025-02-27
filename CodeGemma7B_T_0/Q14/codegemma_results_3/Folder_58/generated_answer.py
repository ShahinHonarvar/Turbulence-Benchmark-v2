def find_second_smallest_num(num_list):
    if len(num_list) < 311 or len(num_list) > 371:
        return 'None'
    num_list = sorted(num_list[310:371])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]