def all_pos_ints_exclusive(numbers):
    if len(numbers) < 2 or numbers[0] > numbers[1] or numbers[0] < 1:
        return []
    return list(range(1, min(numbers[0], numbers[1])))