def find_second_smallest_num(num_list):
    if len(num_list) < 5:
        return None
    sliced_list = num_list[4:5]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]