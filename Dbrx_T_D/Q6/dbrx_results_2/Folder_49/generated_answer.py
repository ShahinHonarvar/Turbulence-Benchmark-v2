def all_neg_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    else:
        return [n for n in numbers[80:200] if n < 0]