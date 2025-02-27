def find_second_smallest_num(numbers):
    subset = sorted(numbers[533:606])
    return subset[1] if len(subset) > 1 else None