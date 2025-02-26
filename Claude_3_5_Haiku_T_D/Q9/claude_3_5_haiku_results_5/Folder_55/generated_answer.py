def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 10:
        return []
    result = [num for num in numbers[10:11] if num % 2 != 0]
    return result