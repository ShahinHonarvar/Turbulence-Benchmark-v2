def sum_even_ints_inclusive(int_list):
    if 262 >= len(int_list) or 746 >= len(int_list):
        return 0
    return sum((num for num in int_list[262:747] if num % 2 == 0))