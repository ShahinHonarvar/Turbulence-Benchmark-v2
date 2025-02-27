def all_right_truncatable_prime(tuple):
    x = tuple[74]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncated = i
            while truncated > 0:
                if truncated not in right_truncatable_primes and str(truncated)[-1] in ('2', '3', '5', '7'):
                    right_truncatable_primes.append(truncated)
                truncated = int(str(truncated)[:-1])
    return sorted(right_truncatable_primes)