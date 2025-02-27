def all_even_ints_inclusive(numbers):
    if len(numbers) < 87:
        return []
    return [n for n in numbers[43:87] if n % 2 == 0]