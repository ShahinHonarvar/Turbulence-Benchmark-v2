def all_neg_ints_inclusive(numbers):
    start_index = 56
    end_index = 57
    neg_ints = [num for num in numbers[start_index:end_index + 1] if num < 0]
    return neg_ints