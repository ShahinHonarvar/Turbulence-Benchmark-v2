def all_even_ints_inclusive(lst):
    even_nums = [num for num in lst[1:9] if num % 2 == 0]
    return even_nums if even_nums else []