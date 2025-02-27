def all_pos_ints_exclusive(numbers):
    start, end = (598, 767)
    if start < 0 or end > len(numbers) or start > len(numbers) or (start >= end):
        return []
    return [num for num in numbers[start:end] if num > 0]