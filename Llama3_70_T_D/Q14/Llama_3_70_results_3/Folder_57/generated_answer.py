def find_second_smallest_num(numbers):
    subset = numbers[20:31]
    unique_subset = list(set(subset))
    unique_subset.sort()
    if len(unique_subset) < 2:
        return None
    else:
        return unique_subset[1]