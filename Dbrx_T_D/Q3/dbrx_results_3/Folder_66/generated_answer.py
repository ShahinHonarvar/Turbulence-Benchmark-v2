def all_pos_ints_inclusive(numbers):
    pos_numbers = [num for num in numbers if num > 0]
    return pos_numbers[50:55] if len(pos_numbers) >= 50 else []