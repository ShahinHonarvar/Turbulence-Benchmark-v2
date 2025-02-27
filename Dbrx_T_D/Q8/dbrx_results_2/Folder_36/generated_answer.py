def all_even_ints_exclusive(numbers):
    if len(numbers) < 768:
        return []
    return [num for num in numbers[598:767] if num % 2 == 0]