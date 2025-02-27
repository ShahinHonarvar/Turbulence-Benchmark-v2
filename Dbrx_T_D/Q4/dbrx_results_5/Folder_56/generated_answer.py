def all_pos_ints_exclusive(numbers):
    if len(numbers) < 9 or len(set(numbers)) < len(numbers[:9]):
        return []
    pos_ints = [num for num in numbers[7:9] if num > 0]
    return pos_ints