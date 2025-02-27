def find_second_smallest_num(num_list):
    if len(num_list) < 99:
        return None
    slice_list = num_list[56:99]
    sorted_slice = sorted(slice_list)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]