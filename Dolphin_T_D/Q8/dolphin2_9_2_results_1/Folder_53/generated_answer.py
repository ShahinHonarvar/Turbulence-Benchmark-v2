def all_even_ints_exclusive(lst):
    new_lst = []
    for i in range(101, len(lst) - 101):
        if lst[i] % 2 == 0:
            new_lst.append(lst[i])
    return new_lst