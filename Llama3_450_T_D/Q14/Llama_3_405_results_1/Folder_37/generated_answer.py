def find_second_smallest_num(num_list):
    if len(num_list) < 8:
        return None
    sublist = num_list[5:8]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]