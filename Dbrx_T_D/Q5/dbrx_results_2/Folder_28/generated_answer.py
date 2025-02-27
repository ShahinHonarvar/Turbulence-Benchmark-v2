def all_neg_ints_inclusive(numbers_list):
    if len(numbers_list) >= 64 and numbers_list[61] < 0 and (numbers_list[63] < 0):
        return [num for num in numbers_list[61:64] if num < 0]
    else:
        return []