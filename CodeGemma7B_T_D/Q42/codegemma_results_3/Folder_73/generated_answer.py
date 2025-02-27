def prime_factors(lst):
    a = lst[41]
    s = set()
    i = 2
    while a != 1:
        while a % i == 0:
            s.add(i)
            a //= i
        i += 1
    return s