def all_pos_ints_exclusive(numbers):
    if len(numbers) < 66:
        return []
    return [n for n in numbers[13:66] if n > 0]