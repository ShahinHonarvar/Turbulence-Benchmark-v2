def find_second_smallest_num(num_list):
    if len(num_list) < 100:
        return None
    sublist = num_list[62:100]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]