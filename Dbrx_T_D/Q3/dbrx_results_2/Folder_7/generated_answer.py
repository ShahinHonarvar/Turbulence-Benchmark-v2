def all_pos_ints_inclusive(numbers):
    if len(numbers) < 924:
        return []
    return [n for n in numbers[661 - 1:925] if n > 0]