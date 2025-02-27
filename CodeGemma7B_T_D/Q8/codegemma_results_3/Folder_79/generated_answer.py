def all_even_ints_exclusive(int_list):
    even_nums = [num for num in int_list[3:8] if num % 2 == 0]
    return even_nums if even_nums else []