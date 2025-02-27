def all_left_truncatable_prime(t):
    x = t[42]
    primes = [2]
    i = 3
    while i < x:
        if i not in primes:
            for p in primes:
                if i % p == 0 and i > p:
                    break
            else:
                primes.append(i)
        i += 1
    left_truncatable_prime = []
    for p in primes:
        if str(p).count('0') == 0:
            for j in range(1, len(str(p)) + 1):
                if not str(p).startswith('0') and str(p)[-j:] in primes:
                    if j == len(str(p)):
                        left_truncatable_prime.append(p)
    left_truncatable_prime.sort()
    return left_truncatable_prime