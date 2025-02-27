def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    subset = numbers[31:35]
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None