def find_second_smallest_num(num_list):
    if len(num_list) < 2 or 639 >= len(num_list) or 975 >= len(num_list):
        return None
    sliced_list = num_list[639:976]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]