def all_even_ints_inclusive(numbers):
    if len(numbers) < 987:
        return []
    return [n for n in numbers[686:988] if n % 2 == 0]