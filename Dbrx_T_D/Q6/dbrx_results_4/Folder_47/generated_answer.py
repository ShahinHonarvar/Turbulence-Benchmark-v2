def all_neg_ints_exclusive(numbers):
    if len(numbers) < 80:
        return []
    return [num for num in numbers[64:80] if num < 0]