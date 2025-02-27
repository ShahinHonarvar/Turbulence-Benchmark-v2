def all_pos_ints_exclusive(numbers):
    lower_index = 48
    upper_index = 76
    return [num for num in numbers[lower_index:upper_index] if num > 0]