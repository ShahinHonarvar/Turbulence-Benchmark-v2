def all_even_ints_inclusive(numbers):
    if len(numbers) < 64:
        return []
    start, end = (62, 63)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]