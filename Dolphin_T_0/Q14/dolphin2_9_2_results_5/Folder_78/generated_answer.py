def find_second_smallest_num(input_list):
    if isinstance(input_list, list) and len(input_list) > 78:
        slice_list = input_list[17:79]
        if len(slice_list) > 1:
            sorted_slice = sorted(set(slice_list))
            if len(sorted_slice) > 1:
                return sorted_slice[1]
    return None