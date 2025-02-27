def all_even_ints_exclusive(numbers):
    if len(numbers) <= 94:
        return []
    return [num for num in numbers[19:94] if num % 2 == 0]