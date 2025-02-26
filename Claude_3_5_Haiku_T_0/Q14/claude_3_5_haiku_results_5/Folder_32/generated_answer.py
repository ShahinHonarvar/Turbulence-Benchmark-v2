def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    subset = numbers[32:36]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]