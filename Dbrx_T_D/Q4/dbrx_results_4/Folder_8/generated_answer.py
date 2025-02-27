def all_pos_ints_exclusive(numbers):
    if len(numbers) < 92:
        return []
    pos_ints = [n for n in numbers[56:92] if n > 0]
    return pos_ints