def all_even_ints_inclusive(lst):
    even_lst = []
    for i in range(56, 58):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    return even_lst