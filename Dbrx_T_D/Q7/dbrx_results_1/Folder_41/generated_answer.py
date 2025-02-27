def all_even_ints_inclusive(numbers):
    if len(numbers) > 6:
        start, end = (6, 6)
        return [num for num in numbers[start:end + 1] if num % 2 == 0]
    else:
        return []