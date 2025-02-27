def all_even_ints_inclusive(lst):
    even_lst = [num for num in lst[52:72] if num % 2 == 0]
    if not even_lst:
        even_lst = []
    return even_lst