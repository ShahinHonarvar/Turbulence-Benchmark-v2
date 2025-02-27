def all_even_ints_inclusive(numbers):
    if len(numbers) >= 200:
        return list(set(numbers[80:201])) if set(numbers[80:201]) & set(range(0, 1000, 2)) else []
    else:
        return []