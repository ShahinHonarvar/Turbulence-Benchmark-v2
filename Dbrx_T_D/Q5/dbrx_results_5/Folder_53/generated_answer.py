def all_neg_ints_inclusive(numbers):
    if len(numbers) < 201:
        return []
    else:
        return [num for num in numbers[100:201] if num < 0]