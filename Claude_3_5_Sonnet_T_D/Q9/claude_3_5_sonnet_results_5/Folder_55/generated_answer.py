def all_odd_ints_inclusive(integer_list):
    if len(integer_list) < 11:
        return []
    return [num for num in integer_list[10:11] if num % 2 != 0]