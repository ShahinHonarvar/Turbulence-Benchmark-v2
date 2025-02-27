def all_neg_ints_inclusive(numbers):
    start = 533
    end = 605
    if end >= len(numbers) or start < 0:
        return []
    return [num for num in numbers[start:end + 1] if num < 0]