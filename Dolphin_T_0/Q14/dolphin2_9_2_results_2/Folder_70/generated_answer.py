def find_second_smallest_num(num_list):
    if 35 <= len(num_list) < 50:
        subset = num_list[35:49]
        if len(set(subset)) > 1:
            sorted_subset = sorted(set(subset))
            return sorted_subset[1]
    return None