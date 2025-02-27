def all_neg_ints_exclusive(numbers):
    if len(numbers) < 376:
        return []
    else:
        return [n for n in numbers[275:376] if n < 0]