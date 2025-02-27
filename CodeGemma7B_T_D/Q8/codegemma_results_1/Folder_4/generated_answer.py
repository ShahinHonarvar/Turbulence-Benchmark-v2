def all_even_ints_exclusive(lst):
    even_list = []
    for i in range(10, 76):
        if lst[i] % 2 == 0:
            even_list.append(lst[i])
    return even_list