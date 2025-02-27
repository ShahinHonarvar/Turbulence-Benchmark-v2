def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 60:
        return []
    result = [num for num in int_list[60:61] if num % 2 != 0]
    return result