def all_odd_ints_inclusive(int_list):
    if len(int_list) < 67:
        return []
    return [num for num in int_list[64:67] if num % 2 != 0]