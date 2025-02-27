def all_left_truncatable_prime(t):
    y = list(range(2, t[23]))

    def isprime(x):
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True
    for i in y:
        if '0' in str(i):
            continue
        a = str(i)
        b = [a[i:] for i in range(len(a))]
        if all((isprime(int(c)) for c in b)):
            y.remove(i)
    return sorted(y)