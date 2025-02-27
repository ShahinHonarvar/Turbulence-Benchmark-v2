def all_right_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(str(i)[-1]) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        for j in range(2, int(str(prime)[-1]) + 1):
            if prime % j == 0:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)