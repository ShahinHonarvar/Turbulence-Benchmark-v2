def find_second_largest_num(numbers):
    if not 25 <= 87 < len(numbers):
        return None
    subset = numbers[25:88]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]