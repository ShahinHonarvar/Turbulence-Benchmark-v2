def all_odd_ints_inclusive(int_list):
    if len(int_list) < 606:
        return []
    return [num for num in int_list[533:606] if num % 2 != 0]