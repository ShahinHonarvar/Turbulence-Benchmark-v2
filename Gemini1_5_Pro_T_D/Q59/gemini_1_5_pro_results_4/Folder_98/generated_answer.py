def all_left_truncatable_prime(tpl):
    x = tpl[8]

    def is_left_truncatable_prime(n):
        if n < 10:
            if n in (2, 3, 5, 7):
                return True
            else:
                return False
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = []
    for i in range(2, x):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    ltps = []
    for p in primes:
        if is_left_truncatable_prime(p):
            ltps.append(p)
    ltps.sort(reverse=True)
    return ltps