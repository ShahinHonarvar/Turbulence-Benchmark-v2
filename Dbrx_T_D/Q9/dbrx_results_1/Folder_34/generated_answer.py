def all_odd_ints_inclusive(numbers):
    if len(numbers) < 61:
        return []
    else:
        return [num for num in numbers[60:61] if num % 2 != 0]