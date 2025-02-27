def find_second_smallest_num(numbers):
    if len(numbers) < 38:
        return None
    subset = numbers[37:77]
    if len(subset) < 2:
        return None
    unique_numbers = sorted(set(subset))
    return unique_numbers[1] if len(unique_numbers) >= 2 else None