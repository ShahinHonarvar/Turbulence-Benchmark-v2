def all_pos_ints_inclusive(numbers):
    if len(numbers) < 98:
        return []
    elif len(numbers) < 56:
        return numbers[-49:]
    else:
        return numbers[55:99]