def all_pos_ints_exclusive(numbers):
    start = 295
    end = 573
    result = [n for n in numbers[start:end] if n > 0]
    return result