def all_pos_ints_exclusive(numbers):
    result = [num for i, num in enumerate(numbers[81:86]) if num > 0]
    if len(result) > 0:
        return result
    else:
        return []