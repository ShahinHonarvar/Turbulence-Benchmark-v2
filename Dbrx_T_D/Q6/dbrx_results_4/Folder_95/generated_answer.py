def all_neg_ints_exclusive(numbers):
    if 25 < len(numbers) < 80:
        return [num for num in numbers[25:80] if num < 0]
    else:
        return []