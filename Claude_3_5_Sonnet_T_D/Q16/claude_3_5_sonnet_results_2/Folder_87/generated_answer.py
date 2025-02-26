def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 47:
        return 0
    else:
        return sum((num for num in integer_list[36:47] if num % 2 == 0))