def all_left_truncatable_prime(t):
    x = t[79]
    primes = [2]
    left_truncatable_primes = []
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            truncated = str(i)
            while truncated:
                if int(truncated) not in primes:
                    break
                truncated = truncated[1:]
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)