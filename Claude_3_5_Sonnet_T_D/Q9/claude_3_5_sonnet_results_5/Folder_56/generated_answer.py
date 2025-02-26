def all_odd_ints_inclusive(numbers):
    if not numbers:
        return []
    return [numbers[0]] if numbers[0] % 2 != 0 else []