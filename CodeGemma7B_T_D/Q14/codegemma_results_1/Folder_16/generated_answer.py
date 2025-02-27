def find_second_smallest_num(num_list):
    if len(num_list) < 66 or len(num_list) < 78:
        return 'None'
    sorted_list = sorted(num_list[66:78])
    if len(sorted_list) < 2:
        return 'None'
    return sorted_list[1]