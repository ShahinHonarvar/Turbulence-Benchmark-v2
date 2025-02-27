def all_left_truncatable_prime(t):
    x = t[92]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1):
        if all((i % p != 0 for p in primes)) and (not '0' in str(i)):
            primes.append(i)
    res = []
    for p in primes:
        if '0' not in str(p):
            i = p
            while i > 1:
                if i in res or i % 10 == 0 or all((i % p != 0 for p in primes)):
                    i //= 10
                else:
                    break
            else:
                res.append(p)
    res.sort()
    return res