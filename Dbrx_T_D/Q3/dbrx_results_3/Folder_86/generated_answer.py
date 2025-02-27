def all_pos_ints_inclusive(numbers):
    start_index = 30
    end_index = 34
    pos_ints = [num for num in numbers[start_index:end_index + 1] if num > 0]
    return pos_ints