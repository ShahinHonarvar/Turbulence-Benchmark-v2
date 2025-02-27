def all_even_ints_exclusive(int_list):
    if len(int_list) < 77:
        return []
    else:
        return [num for num in int_list[10:77:2] if num % 2 == 0]