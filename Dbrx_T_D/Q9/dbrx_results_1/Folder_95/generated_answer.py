def all_odd_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    return [num for num in numbers[82:87] if num % 2 != 0]