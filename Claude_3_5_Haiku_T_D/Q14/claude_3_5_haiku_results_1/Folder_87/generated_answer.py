def find_second_smallest_num(numbers):
    if len(numbers) <= 22:
        return None
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(subset)
    return subset_sorted[1]