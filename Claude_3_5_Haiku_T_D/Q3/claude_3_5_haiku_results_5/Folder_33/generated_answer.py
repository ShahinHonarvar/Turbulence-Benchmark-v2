def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 774:
        return []
    positive_subset = [num for num in numbers[667:775] if num > 0]
    return positive_subset