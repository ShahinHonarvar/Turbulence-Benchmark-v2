def all_even_ints_exclusive(numbers):
    if len(numbers) < 93:
        return []
    return [num for num in numbers[20:93] if num % 2 == 0]