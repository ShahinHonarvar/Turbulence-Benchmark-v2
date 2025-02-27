def all_odd_ints_inclusive(lst):
    L = []
    for n in lst:
        if n >= 31 and n <= 34 and (n % 2 != 0):
            L.append(n)
    return L