def all_even_ints_inclusive(lst):
    even_ints_lst = []
    for i in range(25, 60):
        if lst[i] % 2 == 0:
            even_ints_lst.append(lst[i])
    return even_ints_lst