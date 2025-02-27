def all_even_ints_inclusive(numbers):
    if len(numbers) >= 36:
        start = 33 if len(numbers) > 33 else 0
        return [num for num in numbers[start:37] if num % 2 == 0]
    else:
        return []