def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 111 and i < 473 and (num % 2 == 0)]