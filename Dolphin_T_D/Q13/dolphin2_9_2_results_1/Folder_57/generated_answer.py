def find_second_largest_num(num_list):
    if not 27 <= len(num_list) <= 55:
        return None
    subset = num_list[27:55]
    subset.sort(reverse=True)
    if len(set(subset)) < 2:
        return None
    return subset[1]