def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 69:
        return 0
    return sum((num for num in integer_list[13:69] if num % 2 == 0))