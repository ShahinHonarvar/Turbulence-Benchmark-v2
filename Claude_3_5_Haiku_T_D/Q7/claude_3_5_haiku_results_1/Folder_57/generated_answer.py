def all_even_ints_inclusive(integer_list):
    if len(integer_list) < 56:
        return []
    subset = integer_list[27:56]
    return [num for num in subset if num % 2 == 0]