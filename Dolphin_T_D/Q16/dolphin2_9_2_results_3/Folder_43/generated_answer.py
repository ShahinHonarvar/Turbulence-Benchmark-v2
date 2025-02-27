def sum_even_ints_inclusive(int_list):
    even_ints = [num for num in int_list[68:87] if num % 2 == 0]
    return sum(even_ints) or 0