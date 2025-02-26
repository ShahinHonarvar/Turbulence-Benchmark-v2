def all_odd_ints_inclusive(integer_list):
    if len(integer_list) <= 60:
        return []
    return [num for num in [integer_list[60]] if num % 2 != 0]