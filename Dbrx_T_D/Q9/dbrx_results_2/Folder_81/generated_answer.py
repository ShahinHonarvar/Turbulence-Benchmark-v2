def all_odd_ints_inclusive(numbers):
    if len(numbers) < 101:
        return []
    return [n for n in numbers[9:101] if n % 2 != 0]