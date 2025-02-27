def find_second_smallest_num(num_list):
    if 40 <= 200 < len(num_list):
        subset = num_list[40:201]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
    return None