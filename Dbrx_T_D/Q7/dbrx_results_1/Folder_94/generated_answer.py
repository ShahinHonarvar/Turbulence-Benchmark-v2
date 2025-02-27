def all_even_ints_inclusive(numbers):
    if len(numbers) < 41:
        return []
    result = [num for num in numbers[28:41] if num % 2 == 0]
    return result