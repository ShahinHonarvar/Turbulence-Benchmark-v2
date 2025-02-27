def all_even_ints_exclusive(numbers):
    if len(numbers) < 102:
        return []
    return [n for n in numbers[100:101] if n % 2 == 0]