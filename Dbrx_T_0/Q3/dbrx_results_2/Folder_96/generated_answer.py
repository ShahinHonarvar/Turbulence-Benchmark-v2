def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    pos_ints = [num for num in numbers[50:201] if num > 0]
    return pos_ints