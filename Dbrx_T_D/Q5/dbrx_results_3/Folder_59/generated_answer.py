def all_neg_ints_inclusive(numbers_list):
    return [num for num in numbers_list[:10] if num < 0] if numbers_list[:10] else []