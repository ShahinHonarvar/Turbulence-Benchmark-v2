def all_odd_ints_inclusive(numbers):
    if len(numbers) < 79:
        return []
    return [num for num in numbers[62:79] if num % 2 != 0]