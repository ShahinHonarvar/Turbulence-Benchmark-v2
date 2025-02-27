def all_right_truncatable_prime(t):
    x = t[77]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for p in primes:
        p_str = str(p)
        is_right_truncatable = True
        while len(p_str) > 0:
            if int(p_str) not in primes:
                is_right_truncatable = False
                break
            p_str = p_str[:-1]
        if is_right_truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes, reverse=True)