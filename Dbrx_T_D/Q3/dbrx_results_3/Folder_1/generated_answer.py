def all_pos_ints_inclusive(numbers):
    start_index = 30
    end_index = 72
    return [num for num in numbers[start_index:end_index + 1] if num > 0]