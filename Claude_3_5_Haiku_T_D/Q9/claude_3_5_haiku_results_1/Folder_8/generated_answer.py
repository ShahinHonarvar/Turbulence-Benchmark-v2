def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return []
    target_number = numbers[23]
    if target_number % 2 == 1:
        return [target_number]
    return []