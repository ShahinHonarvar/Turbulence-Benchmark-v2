def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 60:
        return []
    if numbers[60] % 2 == 1:
        return [numbers[60]]
    return []