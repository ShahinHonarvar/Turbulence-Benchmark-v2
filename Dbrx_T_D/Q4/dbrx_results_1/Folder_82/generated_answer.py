def all_pos_ints_exclusive(numbers_list):
    if len(numbers_list) < 200:
        return []
    return [num for num in numbers_list[20:200] if num > 0]