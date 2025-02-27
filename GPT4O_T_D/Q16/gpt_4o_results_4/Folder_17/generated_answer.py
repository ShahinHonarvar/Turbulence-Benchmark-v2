def sum_even_ints_inclusive(int_list):
    if len(int_list) < 79:
        return 0
    return sum((num for num in int_list[62:79] if num % 2 == 0))