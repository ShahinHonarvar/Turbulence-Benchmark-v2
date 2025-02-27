def all_even_ints_exclusive(int_list):
    if len(int_list) <= 51:
        return []
    return [num for num in int_list[52:76] if num % 2 == 0]