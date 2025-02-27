def all_pos_ints_exclusive(numbers):
    if len(numbers) < 67:
        return []
    slice_of_numbers = numbers[43:67]
    return [num for num in slice_of_numbers if num > 0]