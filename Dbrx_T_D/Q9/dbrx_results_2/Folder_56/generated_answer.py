def all_odd_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    return [num for num in numbers if num % 2 != 0][:2]