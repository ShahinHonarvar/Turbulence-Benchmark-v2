def all_pos_ints_exclusive(numbers):
    start = 323
    end = 972
    pos_ints = [num for num in numbers[start:end] if num > 0]
    return pos_ints