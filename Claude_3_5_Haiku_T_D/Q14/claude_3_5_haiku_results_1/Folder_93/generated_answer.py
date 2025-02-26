def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 89:
        return None
    subset = numbers[75:89]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]