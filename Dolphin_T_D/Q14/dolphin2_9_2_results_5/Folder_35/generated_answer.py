def find_second_smallest_num(num_list):
    if len(num_list) < 40:
        return None
    sublist = num_list[15:40]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]