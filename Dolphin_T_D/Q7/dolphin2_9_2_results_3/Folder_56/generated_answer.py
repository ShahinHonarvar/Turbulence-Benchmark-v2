def all_even_ints_inclusive(lst):
    even_ints = []
    if len(lst) > 0:
        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                even_ints.append(lst[i])
    return even_ints