def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    subset = numbers[533:606]
    subset = sorted(set(subset))
    if len(subset) < 2:
        return None
    return subset[1]