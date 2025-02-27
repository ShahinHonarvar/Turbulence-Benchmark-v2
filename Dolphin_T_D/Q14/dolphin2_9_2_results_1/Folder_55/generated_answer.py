def find_second_smallest_num(num_list):
    if len(num_list) != 21:
        return None
    subset = num_list[10:11]
    if len(subset) != 2:
        return None
    subset.sort()
    return subset[1]