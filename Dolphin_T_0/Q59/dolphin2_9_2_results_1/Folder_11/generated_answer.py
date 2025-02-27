def all_left_truncatable_prime(i):
    x = i[86]
    l = [2, 3, 5, 7]
    for m in range(11, x, 2):
        n = m
        while n:
            if n % 10 == 0 or n == 1:
                break
            k = int(str(n)[1:])
            if all((k % s for s in l)):
                l.append(n)
            n = k
    return sorted(l)