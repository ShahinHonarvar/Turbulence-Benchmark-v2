def all_pos_ints_inclusive(numbers):
    if len(numbers) < 87:
        return []
    positive_slice = [num for num in numbers[68:87] if num > 0]
    return positive_slice