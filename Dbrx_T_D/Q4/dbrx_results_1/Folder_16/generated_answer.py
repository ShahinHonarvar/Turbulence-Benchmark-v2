def all_pos_ints_exclusive(numbers):
    if len(numbers) < 90:
        return []
    sublist = numbers[86:90]
    return [num for num in sublist if num > 0]