def find_second_smallest_num(num_list):
    sliced_list = num_list[56:99]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]