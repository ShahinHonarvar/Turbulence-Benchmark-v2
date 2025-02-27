def all_left_truncatable_prime(t):
    x = t[79]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    left_truncatable_primes = []
    for p in primes:
        if '0' not in str(p):
            truncated = str(p)
            while len(truncated) > 0:
                if int(truncated) not in primes:
                    break
                truncated = truncated[1:]
            else:
                left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)