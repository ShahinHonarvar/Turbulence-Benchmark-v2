def find_second_smallest_num(num_list):
    subset = num_list[56:58]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]