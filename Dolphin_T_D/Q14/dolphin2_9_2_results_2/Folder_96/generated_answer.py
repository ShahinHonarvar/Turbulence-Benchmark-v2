def find_second_smallest_num(in_list):
    if in_list:
        sublist = in_list[50:201]
        if len(sublist) >= 2:
            return sorted(sublist)[1]
    return None