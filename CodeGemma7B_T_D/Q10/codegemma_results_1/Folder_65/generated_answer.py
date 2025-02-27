def all_odd_ints_exclusive(int_list):
    if not int_list:
        return []
    result = [num for num in int_list[42:87] if num % 2 != 0]
    return result if result else []