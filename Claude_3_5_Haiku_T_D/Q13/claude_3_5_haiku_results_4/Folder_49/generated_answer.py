def find_second_largest_num(numbers):
    if len(numbers) < 82:
        return None
    subset = numbers[80:201]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None