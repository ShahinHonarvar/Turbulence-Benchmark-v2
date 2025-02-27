def all_even_ints_inclusive(numbers):
    if len(numbers) < 39:
        return []
    return [num for num in numbers[28:39] if num % 2 == 0]