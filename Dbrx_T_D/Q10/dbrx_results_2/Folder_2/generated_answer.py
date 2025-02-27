def all_odd_ints_exclusive(numbers):
    if len(numbers) < 53:
        return []
    return [n for n in numbers[35:52] if n % 2 != 0]