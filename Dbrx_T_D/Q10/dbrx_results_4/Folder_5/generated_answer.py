def all_odd_ints_exclusive(numbers):
    if len(numbers) < 7:
        return []
    return [n for n in numbers[2:7] if n % 2 != 0]