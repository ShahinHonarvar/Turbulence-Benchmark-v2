def find_second_largest_num(numbers):
    subset = numbers[262:747]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[-2]