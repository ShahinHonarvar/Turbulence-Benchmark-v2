def all_even_ints_exclusive(numbers):
    start = 68
    end = 99
    if start < 0 or end >= len(numbers) or start >= end:
        return []
    return [num for num in numbers[start:end] if num % 2 == 0]