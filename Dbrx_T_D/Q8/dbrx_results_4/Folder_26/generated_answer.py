def all_even_ints_exclusive(numbers):
    if len(numbers) <= 78 or len(numbers) < 44:
        return []
    return [num for num in numbers[44:78] if num % 2 == 0]