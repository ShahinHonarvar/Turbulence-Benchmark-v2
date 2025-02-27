def all_even_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    return [n for n in numbers[50:201] if n % 2 == 0]