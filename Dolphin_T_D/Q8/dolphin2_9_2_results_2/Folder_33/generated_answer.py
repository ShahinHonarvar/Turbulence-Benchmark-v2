def all_even_ints_exclusive(lst):
    even_lst = []
    for i in range(369, 983, 2):
        if i in lst:
            even_lst.append(i)
    return even_lst