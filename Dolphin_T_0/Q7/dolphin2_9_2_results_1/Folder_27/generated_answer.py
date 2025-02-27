def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(66, 94):
        if i in lst and i % 2 == 0:
            even_ints.append(i)
    return even_ints