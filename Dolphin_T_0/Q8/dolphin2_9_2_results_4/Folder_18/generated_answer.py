def all_even_ints_exclusive(lst):
    even_numbers = [num for num in lst[58:84] if num % 2 == 0]
    return even_numbers if even_numbers else []