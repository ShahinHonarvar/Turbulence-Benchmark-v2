def all_even_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    even_numbers = [n for n in numbers[30:200] if n % 2 == 0]
    return even_numbers