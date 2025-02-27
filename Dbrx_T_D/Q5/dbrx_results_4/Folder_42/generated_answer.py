def all_neg_ints_inclusive(numbers):
    return [num for num in numbers[29:80] if num < 0] if 29 < len(numbers) and 80 <= len(numbers) else []