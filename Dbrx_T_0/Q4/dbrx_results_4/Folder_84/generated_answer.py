def all_pos_ints_exclusive(numbers):
    if len(numbers) < 92:
        return []
    pos_ints = [num for num in numbers[50:92] if num > 0]
    return pos_ints