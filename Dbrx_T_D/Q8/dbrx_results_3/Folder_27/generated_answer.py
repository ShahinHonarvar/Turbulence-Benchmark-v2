def all_even_ints_exclusive(int_list):
    if len(int_list) < 49 or 28 > len(int_list):
        return []
    else:
        return [num for num in int_list[28:49:2] if num % 2 == 0]