def all_right_truncatable_primes(t):
    truf = []
    for n in range(t[0]):
        a = str(n)
        b = a
        for i in range(1, len(a)):
            b = b[:-1]
            if not isprime(int(b)):
                break
        else:
            if isprime(int(a)):
                truf.append(int(a))
    return sorted(truf, reverse=True)