def all_even_ints_inclusive(lst):
    lst = lst[6:9]
    even_lst = [i for i in lst if i % 2 == 0]
    if not even_lst:
        even_lst = []
    return even_lst