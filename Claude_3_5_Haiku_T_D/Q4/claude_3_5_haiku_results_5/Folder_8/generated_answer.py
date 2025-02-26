def all_pos_ints_exclusive(numbers):
    if len(numbers) <= 57:
        return []
    slice_range = numbers[57:92]
    positive_nums = [num for num in slice_range if num > 0]
    return positive_nums