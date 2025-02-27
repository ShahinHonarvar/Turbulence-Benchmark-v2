def all_odd_ints_inclusive(numbers):
    if len(numbers) < 98:
        return []
    result = [num for num in numbers[56:99] if num % 2 != 0]
    return result