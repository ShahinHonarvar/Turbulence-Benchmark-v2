def sum_even_ints_inclusive(int_list):
    if len(int_list) < 10:
        return 0
    return sum((num for num in int_list[8:10] if num % 2 == 0))