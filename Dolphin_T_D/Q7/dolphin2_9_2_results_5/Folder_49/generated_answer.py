def all_even_ints_inclusive(lst):
    even_ints = [num for num in lst[80:201] if num % 2 == 0]
    return even_ints if even_ints else []