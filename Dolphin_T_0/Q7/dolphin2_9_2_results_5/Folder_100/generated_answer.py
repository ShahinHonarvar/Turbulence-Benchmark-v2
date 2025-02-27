def all_even_ints_inclusive(lst):
    even_list = [num for num in lst[42:69] if num % 2 == 0]
    return even_list if even_list else []