def all_even_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    start, end = (21, 97)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]