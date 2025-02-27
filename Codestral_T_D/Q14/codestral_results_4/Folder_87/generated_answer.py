def find_second_smallest_num(numbers):
    subset = sorted(numbers[22:89])
    if len(subset) < 2:
        return None
    return subset[1]