def all_pos_ints_exclusive(numbers):
    indices = list(range(276, 376))
    result = [numbers[i] for i in indices if numbers[i] > 0]
    return result