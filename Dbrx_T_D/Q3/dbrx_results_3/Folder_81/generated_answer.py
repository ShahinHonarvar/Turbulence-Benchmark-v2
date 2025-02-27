def all_pos_ints_inclusive(numbers):
    start = 10
    end = 100
    pos_ints = [num for num in numbers[start:end + 1] if num > 0]
    return pos_ints