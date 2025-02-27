def all_neg_ints_inclusive(numbers):
    return [num for num in numbers[80:201] if num < 0] if len(numbers) >= 201 else []