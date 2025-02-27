def all_neg_ints_inclusive(numbers_list):
    if len(numbers_list) >= 8:
        return [num for num in numbers_list[5:8] if num < 0]
    else:
        return []