def all_left_truncatable_prime(t):
    x = t[10]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        is_truncatable = True
        for i in range(1, len(p_str)):
            if int(p_str[i:]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)