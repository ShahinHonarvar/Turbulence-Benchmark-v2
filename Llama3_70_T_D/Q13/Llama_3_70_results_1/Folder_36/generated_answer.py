def find_second_largest_num(num_list):
    sliced_list = num_list[246:751]
    sorted_list = sorted(sliced_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]