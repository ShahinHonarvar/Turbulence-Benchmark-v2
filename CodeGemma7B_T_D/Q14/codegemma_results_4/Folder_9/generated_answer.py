def find_second_smallest_num(num_list):
    sorted_list = sorted(num_list)
    if len(sorted_list) < 200:
        return 'None'
    return sorted_list[70]