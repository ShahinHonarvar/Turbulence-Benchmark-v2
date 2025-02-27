def all_left_truncatable_prime(t):
    x = t[1]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            truncated = str(i)
            while truncated:
                if int(truncated) not in primes:
                    break
                truncated = truncated[1:]
            else:
                primes.append(i)
    return sorted(primes, reverse=True)