def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 538:
        return []
    return [n for n in numbers[527:539] if n > 0]