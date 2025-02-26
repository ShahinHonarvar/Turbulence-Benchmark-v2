def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[4:5]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]