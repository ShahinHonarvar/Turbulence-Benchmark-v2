def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    subset = numbers[25:60]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]