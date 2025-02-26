def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 79:
        return []
    return [num for num in numbers[29:80] if num % 2 != 0]