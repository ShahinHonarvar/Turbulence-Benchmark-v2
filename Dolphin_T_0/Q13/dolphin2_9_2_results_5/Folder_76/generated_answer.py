def find_second_largest_num(numbers):
    subset = numbers[686:988]
    if len(subset) < 2:
        return None
    else:
        sorted_subset = sorted(subset, reverse=True)
        return sorted_subset[1]