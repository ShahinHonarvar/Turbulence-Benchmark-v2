def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    subset = numbers[59:98]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None