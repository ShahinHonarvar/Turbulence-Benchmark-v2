def all_even_ints_inclusive(int_list):
    subset = int_list[42:69]
    return [num for num in subset if num % 2 == 0]