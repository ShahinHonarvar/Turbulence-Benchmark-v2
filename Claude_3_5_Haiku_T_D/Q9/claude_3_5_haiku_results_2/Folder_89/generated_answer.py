def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 82:
        return []
    return [num for num in numbers[56:83] if num % 2 != 0]