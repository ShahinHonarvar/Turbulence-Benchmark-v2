def all_right_truncatable_prime(n):
    a, b, l = (n[0], n[1], [])
    while a != 0:
        l += [a]
        a = int(str(a)[-1])
    l = [i for i in l if all((str(i) % d != 0 for d in range(2, int(str(i)[-1]) + 1)))]
    l.sort()
    return l