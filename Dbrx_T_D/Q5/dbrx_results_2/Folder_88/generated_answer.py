def all_neg_ints_inclusive(numbers):
    start = 4
    end = 8
    if len(numbers) > end:
        return [num for num in numbers[start:end + 1] if isinstance(num, int) and num < 0]
    else:
        return []