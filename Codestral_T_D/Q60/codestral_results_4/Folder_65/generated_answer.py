def all_left_right_truncatable_prime(tup):
    x = tup[32]
    primes = [2]
    for i in range(3, x + 1, 2):
        if all((i % p > 0 for p in primes)) and '0' not in str(i):
            primes.append(i)

    def is_truncatable(p):
        p_str = str(p)
        return all((int(p_str[i:]) in primes and int(p_str[:-i]) in primes for i in range(1, len(p_str))))
    return sorted((p for p in primes if is_truncatable(p)))