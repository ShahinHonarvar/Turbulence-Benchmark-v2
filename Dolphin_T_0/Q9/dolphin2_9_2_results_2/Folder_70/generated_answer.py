def all_odd_ints_inclusive(numbers):
    result = [num for num in numbers[28:33] if num % 2 != 0]
    if len(result) == 0:
        return []
    else:
        return result