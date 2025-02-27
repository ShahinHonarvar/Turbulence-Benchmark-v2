def all_even_ints_inclusive(lst):
    even_lst = [num for index, num in enumerate(lst[32:36]) if num % 2 == 0 and 32 <= index <= 35]
    return even_lst if even_lst else []