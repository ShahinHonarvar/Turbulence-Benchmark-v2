def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 92:
        return None
    subset = numbers[90:201]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]