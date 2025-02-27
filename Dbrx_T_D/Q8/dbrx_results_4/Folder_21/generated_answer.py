def all_even_ints_exclusive(numbers):
    start, end = (743, 867)
    if start < 0 or end > len(numbers) or start >= end:
        return []
    return [num for num in numbers[start:end] if num % 2 == 0]