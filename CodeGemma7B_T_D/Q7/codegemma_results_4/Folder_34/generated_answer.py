def all_even_ints_inclusive(lst):
    lst2 = []
    for i in lst:
        if i >= 60 and i <= 200 and (i % 2 == 0):
            lst2.append(i)
    return lst2