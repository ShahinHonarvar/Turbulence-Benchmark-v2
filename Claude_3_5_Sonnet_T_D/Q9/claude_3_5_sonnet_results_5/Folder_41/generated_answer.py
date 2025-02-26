def all_odd_ints_inclusive(numbers):
    if len(numbers) > 6:
        return [num for num in numbers[6:7] if num % 2 != 0]
    else:
        return []