def find_second_largest_num(numbers):
    if len(numbers) < 86 or len(numbers[70:85]) < 2:
        return None
    subset = numbers[70:85]
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None