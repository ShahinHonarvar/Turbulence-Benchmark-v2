def find_second_smallest_num(num_list):
    second_smallest = None
    slice_list = sorted(num_list[639:976])
    if len(slice_list) > 1:
        second_smallest = slice_list[1]
    return second_smallest