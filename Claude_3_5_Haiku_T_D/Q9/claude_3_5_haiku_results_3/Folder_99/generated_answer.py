def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 370:
        return []
    return [num for num in int_list[310:371] if num % 2 != 0]