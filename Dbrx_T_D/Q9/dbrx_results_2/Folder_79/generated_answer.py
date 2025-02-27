def all_odd_ints_inclusive(numbers):
    if len(numbers) < 5:
        return []
    else:
        return [num for num in numbers[4:] if num % 2 != 0]