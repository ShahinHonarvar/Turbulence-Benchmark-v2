def all_even_ints_inclusive(lst):
    result = []
    for i in range(21, 98):
        if i in lst and i % 2 == 0:
            result.append(i)
    return result