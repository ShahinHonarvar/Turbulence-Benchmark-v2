def all_neg_ints_inclusive(numbers):
    if len(numbers) < 35:
        return []
    else:
        return [num for num in numbers[31:35] if num < 0]