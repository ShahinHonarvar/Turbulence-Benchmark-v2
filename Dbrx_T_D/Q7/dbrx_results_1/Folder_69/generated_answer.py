def all_even_ints_inclusive(numbers):
    if len(numbers) < 36 or len(numbers) < 33:
        return []
    return [num for num in numbers[32:36] if num % 2 == 0]