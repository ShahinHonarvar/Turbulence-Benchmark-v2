def all_odd_ints_inclusive(numbers):
    if len(numbers) < 2:
        return [num for num in numbers if num % 2 != 0]
    return [num for num in numbers[:2] if num % 2 != 0]