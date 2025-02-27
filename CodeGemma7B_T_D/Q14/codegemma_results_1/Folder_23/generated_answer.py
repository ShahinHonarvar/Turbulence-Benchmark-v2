def find_second_smallest_num(num_list):
    num_list_sliced = sorted(num_list[19:93])
    if len(num_list_sliced) < 2:
        return None
    else:
        return num_list_sliced[1]