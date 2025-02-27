def find_second_smallest_num(data):
    if len(data) < 49 or len(data) < 36:
        return None
    subset = data[35:50]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]