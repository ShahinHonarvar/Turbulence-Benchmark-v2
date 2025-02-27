def all_left_truncatable_prime(integers):
    x = integers[18]
    primes = [2, 3, 5, 7]
    for n in range(11, x):
        if (n % 2 == 0 or n == 1) and n != 2:
            pass
        else:
            c = 0
            for i in range(2, int(n / 2) + 1):
                if n % i == 0 and i != 1:
                    c += 1
                    break
            if c == 0:
                primes.append(n)
    lt_primes = []
    for prime in primes:
        f = True
        s = str(prime)
        m = len(s)
        for i in range(m - 1):
            if int(s[i + 1:m]) in primes:
                pass
            else:
                f = False
        if f:
            lt_primes.append(prime)
    lt_primes.sort(reverse=True)
    return lt_primes