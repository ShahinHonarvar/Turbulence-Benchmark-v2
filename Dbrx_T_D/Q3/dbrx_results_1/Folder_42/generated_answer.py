def all_pos_ints_inclusive(numbers):
    start_index = 29
    end_index = 79
    if start_index < 0 or end_index > len(numbers) - 1:
        raise IndexError('Index out of range')
    pos_ints = [num for num in numbers[start_index:end_index + 1] if num > 0]
    return pos_ints