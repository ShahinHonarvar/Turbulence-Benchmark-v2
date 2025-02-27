def all_pos_ints_inclusive(numbers):
    if len(numbers) < 50:
        return []
    result = [n for n in numbers[22:51] if n > 0]
    return result