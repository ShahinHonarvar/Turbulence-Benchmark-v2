def all_left_truncatable_prime(t):
    x = t[88]
    lst = []
    for i in range(10 ** (len(str(x)) - 1), x):
        if all((str(i)[j:] and int(str(i)[j:]) in [2, 3, 5, 7] for j in range(len(str(i)) - 1))):
            lst.append(i)
    return sorted(lst, reverse=True)