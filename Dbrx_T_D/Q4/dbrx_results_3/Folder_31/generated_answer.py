def all_pos_ints_exclusive(numbers):
    if len(numbers) < 95:
        return []
    return [n for n in numbers[87:95] if n > 0]