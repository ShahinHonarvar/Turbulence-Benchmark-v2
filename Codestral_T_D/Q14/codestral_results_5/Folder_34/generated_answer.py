def find_second_smallest_num(num_list):
    num_list_slice = num_list[60:201]
    num_list_slice.sort()
    if len(num_list_slice) < 2:
        return None
    return num_list_slice[1]