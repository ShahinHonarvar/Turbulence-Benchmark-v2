def find_second_smallest_num(list):
    sorted_list = sorted(list[686:988])
    if len(sorted_list) < 2:
        return 'None'
    else:
        return sorted_list[1]