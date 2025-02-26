def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 688:
        return None
    subset = numbers[686:988]
    if not subset:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None