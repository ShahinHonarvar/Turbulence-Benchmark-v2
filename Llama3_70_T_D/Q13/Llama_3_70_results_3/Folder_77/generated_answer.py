def find_second_largest_num(num_list):
    slice_list = num_list[527:539]
    slice_list.sort(reverse=True)
    if len(slice_list) < 2:
        return None
    return slice_list[1]