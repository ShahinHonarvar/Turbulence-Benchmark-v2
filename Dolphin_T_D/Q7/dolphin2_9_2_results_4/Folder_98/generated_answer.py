def all_even_ints_inclusive(lst):
    even_lst = [num for i, num in enumerate(lst) if num % 2 == 0 and 0 <= i <= 6]
    return even_lst