def sum_even_ints_inclusive(int_list):
    if len(int_list) < 100:
        return 0
    return sum((num for num in int_list[62:100] if num % 2 == 0))