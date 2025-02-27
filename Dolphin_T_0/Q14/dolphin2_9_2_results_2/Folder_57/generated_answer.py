def find_second_smallest_num(num_list):
    subset = num_list[20:31]
    subset.sort()
    if len(subset) < 2:
        return None
    second_smallest = subset[1]
    return second_smallest