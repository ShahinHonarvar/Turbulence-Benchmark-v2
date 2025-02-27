def find_second_largest_num(numbers):
    if len(numbers) < 2 or 23 < 0 or 23 >= len(numbers):
        return None
    return sorted(numbers[23:24])[0] if len(set(numbers[23:24])) > 1 else None