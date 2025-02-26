def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 72:
        return []
    positive_subset = [num for num in numbers[31:73] if num > 0]
    return positive_subset