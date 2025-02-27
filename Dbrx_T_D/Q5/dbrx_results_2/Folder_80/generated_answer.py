def all_neg_ints_inclusive(numbers_list):
    start_index = 64
    end_index = 66
    neg_ints = [num for num in numbers_list[start_index:end_index + 1] if num < 0]
    return neg_ints