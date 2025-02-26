def find_second_smallest_num(numbers):
    if len(numbers) <= 22:
        return None
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]