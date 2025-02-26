def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 88:
        return 0
    return sum((num for num in integer_list[25:88] if num % 2 == 0))