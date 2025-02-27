def all_pos_ints_exclusive(numbers):
    if len(numbers) < 45 or 23 > len(numbers):
        return []
    return [num for num in numbers[23:45] if num > 0]