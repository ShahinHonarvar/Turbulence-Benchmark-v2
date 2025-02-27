def all_pos_ints_inclusive(numbers_list):
    if len(numbers_list) >= 93:
        return [num for num in numbers_list[19:93] if num > 0]
    else:
        return []