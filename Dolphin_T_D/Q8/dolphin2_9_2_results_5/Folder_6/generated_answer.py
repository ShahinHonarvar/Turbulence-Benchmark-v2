def all_even_ints_exclusive(lst):
    even_ints = []
    for int in lst[86:99]:
        if int % 2 == 0:
            even_ints.append(int)
    return even_ints