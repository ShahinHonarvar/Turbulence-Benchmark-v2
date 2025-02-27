def all_pos_ints_inclusive(numbers):
    if len(numbers) < 10:
        return []
    sublist = numbers[8:10]
    return [num for num in sublist if num > 0]