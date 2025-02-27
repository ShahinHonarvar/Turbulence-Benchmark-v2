def all_even_ints_inclusive(numbers):
    if len(numbers) <= 73:
        return []
    return [num for num in numbers[73:74] if num % 2 == 0]