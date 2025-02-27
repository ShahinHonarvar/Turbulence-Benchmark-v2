def all_pos_ints_inclusive(numbers_list):
    if len(numbers_list) >= 41 and isinstance(numbers_list[27], int) and isinstance(numbers_list[40], int):
        return [num for num in numbers_list[28:41] if num > 0]
    else:
        return []