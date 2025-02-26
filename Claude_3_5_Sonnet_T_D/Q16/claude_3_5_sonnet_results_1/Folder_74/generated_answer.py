def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 79:
        return 0
    return sum((num for num in integer_list[17:79] if num % 2 == 0))