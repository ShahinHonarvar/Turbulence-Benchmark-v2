def find_second_largest_num(numbers):
    if len(numbers) < 32:
        return None
    subset = numbers[30:201]
    if len(subset) == 0:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None