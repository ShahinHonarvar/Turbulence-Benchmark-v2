def all_even_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    return [num for num in numbers[50:55] if num % 2 == 0]