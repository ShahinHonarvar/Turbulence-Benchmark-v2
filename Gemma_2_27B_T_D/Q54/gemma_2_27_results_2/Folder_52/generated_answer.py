def all_right_truncatable_prime(numbers):
    x = numbers[52]
    primes = []
    for i in range(2, x):
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
        for i in range(len(p_str) - 1, 0, -1):
            truncated = int(p_str[:i])
            is_prime = True
            for j in range(2, int(truncated ** 0.5) + 1):
                if truncated % j == 0:
                    is_prime = False
                    break
            if not is_prime:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)