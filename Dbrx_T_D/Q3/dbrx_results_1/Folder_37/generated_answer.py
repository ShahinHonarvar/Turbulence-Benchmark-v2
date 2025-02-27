def all_pos_ints_inclusive(numbers_list):
    if len(numbers_list) >= 6 and all((isinstance(num, int) for num in numbers_list[:6])):
        return list(filter(lambda x: x > 0, numbers_list[1:6]))
    else:
        return []