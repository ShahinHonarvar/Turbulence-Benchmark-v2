def all_pos_ints_exclusive(numbers):
    start = 10
    end = 100
    pos_ints = [num for num in numbers[start:end] if num > 0]
    return pos_ints[1:-1]