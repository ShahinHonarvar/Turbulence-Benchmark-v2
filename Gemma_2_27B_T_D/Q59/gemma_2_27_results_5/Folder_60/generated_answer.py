def all_left_truncatable_prime(t):
    x = t[87]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = []
    for p in primes:
        s = str(p)
        is_left_truncatable = True
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(p)
    return sorted(result)