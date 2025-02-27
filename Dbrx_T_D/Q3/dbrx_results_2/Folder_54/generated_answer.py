def all_pos_ints_inclusive(numbers_list):
    if len(numbers_list) >= 56 and all((isinstance(num, int) for num in numbers_list[34:56])):
        return [num for num in numbers_list[34:56] if num > 0]
    else:
        return []