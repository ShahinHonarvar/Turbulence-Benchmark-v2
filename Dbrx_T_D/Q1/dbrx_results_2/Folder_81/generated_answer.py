def all_ints_inclusive(numbers):
    if not isinstance(numbers, list) or len(numbers) < 101:
        return 'Input is not a valid list of integers.'
    return numbers[10:11] + numbers[99:101]