def all_neg_ints_inclusive(numbers):
    if len(numbers) < 92:
        return []
    return [num for num in numbers[62:93] if num < 0]