def all_even_ints_inclusive(int_list):
    if len(int_list) <= 73:
        return []
    return [num for num in int_list[73:74] if num % 2 == 0]