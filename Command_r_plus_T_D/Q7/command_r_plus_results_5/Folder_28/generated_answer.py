def all_even_ints_inclusive(int_list):
    if len(int_list) > 63:
        return [num for num in int_list[62:64] if num % 2 == 0]
    else:
        return []