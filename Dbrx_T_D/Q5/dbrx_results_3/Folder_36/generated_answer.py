def all_neg_ints_inclusive(numbers_list):
    start_index = 246
    end_index = 750
    return [num for num in numbers_list[start_index:end_index + 1] if num < 0]