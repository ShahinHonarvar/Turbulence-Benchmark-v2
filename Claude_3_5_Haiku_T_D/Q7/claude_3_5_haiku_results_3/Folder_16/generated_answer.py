def all_even_ints_inclusive(numbers):
    if len(numbers) < 37:
        return []
    result = [num for num in numbers[33:37] if num % 2 == 0]
    return result