def find_second_smallest_num(numbers):
    if len(numbers) <= 82:
        return None
    subset = numbers[56:83]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]