def all_neg_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    result = [num for num in numbers[20:201] if num < 0]
    return result