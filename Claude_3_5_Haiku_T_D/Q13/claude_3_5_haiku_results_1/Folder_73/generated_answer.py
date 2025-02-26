def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    subset = numbers[19:93]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset_without_largest = [num for num in subset if num != largest]
    if not subset_without_largest:
        return None
    return max(subset_without_largest)