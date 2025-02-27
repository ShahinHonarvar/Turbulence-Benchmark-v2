def all_odd_ints_exclusive(numbers):
    if len(numbers) < 12:
        return []
    return [n for n in numbers[10:12] if n % 2 != 0]