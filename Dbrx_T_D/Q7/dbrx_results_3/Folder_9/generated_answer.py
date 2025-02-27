def all_even_ints_inclusive(numbers):
    if len(numbers) < 74 or len(numbers) < 147:
        return []
    else:
        return [num for num in numbers[73:148] if num % 2 == 0]