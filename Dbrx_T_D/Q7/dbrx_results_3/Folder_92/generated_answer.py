def all_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    start, end = (min(0, numbers[0]), max(1, numbers[1]))
    return [n for n in numbers[start:end + 1] if n % 2 == 0]