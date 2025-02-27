def all_even_ints_exclusive(numbers):
    if len(numbers) < 80:
        return []
    return [n for n in numbers[25:80:2] if n % 2 == 0]