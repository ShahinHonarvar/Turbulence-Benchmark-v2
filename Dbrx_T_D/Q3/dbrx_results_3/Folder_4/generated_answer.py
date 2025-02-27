def all_pos_ints_inclusive(numbers):
    if not numbers or len(numbers) < 92:
        return []
    return [num for num in numbers[:93] if num > 0]