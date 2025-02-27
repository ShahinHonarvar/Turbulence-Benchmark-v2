def all_left_truncatable_prime(a):
    b = len(a) - 1
    c = a[97] - 1

    def left_truncatable_prime(n):
        return all((int(''.join(str(n)[:i])) != 0 and isPrime(int(''.join(str(n)[:i]))) for i in range(1, len(str(n)))))
    if c == 3 or c == 2:
        d = [p for p in [2 ** e * 3 ** f + 1 for e in range(1, c + 1) for f in range(1, c + 1)] if left_truncatable_prime(p)]
        return d
    e = [2, 3, 5, 7, 11, 13, 17]
    f = [2, 3]
    g = [2 * i for i in f]
    h = [5 * i for i in f]
    i = 1
    for j in range(2, c):
        i *= j
    j = [p for p in e if p < c and left_truncatable_prime(p)]
    k = [p for p in f if p ** j[-1] < c and left_truncatable_prime(p ** j[-1])]
    l = [p for p in g if p ** j[-1] < c and left_truncatable_prime(p ** j[-1])]
    m = [p for p in h if p ** j[-1] < c and left_truncatable_prime(p ** j[-1])]
    n = [p ** k[i] ** j[-1] for i in range(len(k)) if p ** k[i] ** j[-1] < c and left_truncatable_prime(p ** k[i] ** j[-1])]
    o = [p ** l[i] ** j[-1] for i in range(len(l)) if p ** l[i] ** j[-1] < c and left_truncatable_prime(p ** l[i] ** j[-1])]
    p = [p ** m[i] ** j[-1] for i in range(len(m)) if p ** m[i] ** j[-1] < c and left_truncatable_prime(p ** m[i] ** j[-1])]
    r = j + k + l + m + n + o + p
    return sorted([str(p) for p in r])