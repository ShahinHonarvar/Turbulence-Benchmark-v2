def find_second_smallest_num(numbers):
    if len(numbers) < 57:
        return None
    subset = numbers[56:99]
    if not subset:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]