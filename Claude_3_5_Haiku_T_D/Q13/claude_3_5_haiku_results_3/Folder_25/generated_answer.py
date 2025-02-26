def find_second_largest_num(numbers):
    if len(numbers) < 30 or not 29 <= len(numbers) - 1:
        return None
    subset = numbers[29:94]
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None