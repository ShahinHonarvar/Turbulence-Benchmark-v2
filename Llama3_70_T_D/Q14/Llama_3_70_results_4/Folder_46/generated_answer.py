def find_second_smallest_num(num_list):
    if len(num_list) < 69:
        return None
    sublist = num_list[13:69]
    sorted_list = sorted(sublist)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]