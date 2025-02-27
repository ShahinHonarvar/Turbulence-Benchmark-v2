def all_pos_ints_exclusive(numbers):
    start_index = 93
    end_index = 94
    if end_index < start_index or end_index > len(numbers):
        return []
    return [num for num in numbers[start_index:end_index] if num > 0]