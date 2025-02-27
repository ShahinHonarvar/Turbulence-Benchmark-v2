def all_left_truncatable_prime(t):
    x = t[86]
    primes = [i for i in range(x, 1, -1) if is_prime(i) and is_left_truncatable(i)]
    return sorted(primes, reverse=True)