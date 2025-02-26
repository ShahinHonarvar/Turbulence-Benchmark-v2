def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[62:100]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(subset, reverse=True)
    return subset_sorted[1]