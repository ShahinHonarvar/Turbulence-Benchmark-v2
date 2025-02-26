def sum_even_ints_inclusive(int_list):
    if len(int_list) < 9:
        return sum((num for num in int_list[1:] if num % 2 == 0))
    else:
        return sum((num for num in int_list[1:9] if num % 2 == 0))