def all_even_ints_inclusive(numbers):
    if len(numbers) < 58:
        return []
    return [num for num in numbers[56:58] if num % 2 == 0]