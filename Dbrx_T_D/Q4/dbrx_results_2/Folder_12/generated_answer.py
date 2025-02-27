def all_pos_ints_exclusive(numbers):
    if len(numbers) < 45:
        return []
    else:
        return [n for n in numbers[22:45] if n > 0]