def all_pos_ints_inclusive(numbers):
    return [number for i, number in enumerate(numbers) if number > 0 and 0 <= i <= 10]