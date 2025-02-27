def find_second_smallest_num(num_list):
    subset = num_list[24:88]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]