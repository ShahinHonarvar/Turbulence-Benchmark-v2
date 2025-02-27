def all_even_ints_exclusive(lst):
    even_nums = [num for num in lst[295:573] if num % 2 == 0]
    return even_nums if even_nums else []