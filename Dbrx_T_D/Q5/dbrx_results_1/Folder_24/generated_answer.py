def all_neg_ints_inclusive(numbers_list):
    if len(numbers_list) < 95:
        return []
    return [num for num in numbers_list[74:96] if num < 0]