def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(0, 2):
        if i % 2 == 0:
            even_ints.append(i)
    if even_ints == []:
        return []
    else:
        return even_ints