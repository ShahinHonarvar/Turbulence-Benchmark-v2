def all_even_ints_inclusive(lst):
    even_lst = [num for num in lst[80:201] if num % 2 == 0]
    return even_lst if even_lst else []