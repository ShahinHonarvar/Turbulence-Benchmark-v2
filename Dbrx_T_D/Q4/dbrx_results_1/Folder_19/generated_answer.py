def all_pos_ints_exclusive(numbers):
    start, end = (2, 5)
    if start < 0 or end > len(numbers) or start >= end:
        return []
    return [n for n in numbers[start:end] if n > 0]