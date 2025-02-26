def find_second_largest_num(numbers):
    if len(numbers) < 42 or 40 >= len(numbers):
        return None
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]