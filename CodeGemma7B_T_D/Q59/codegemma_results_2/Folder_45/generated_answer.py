def all_left_truncatable_prime(x):
    primes = [p for p in range(2, x) if all((p % d != 0 for d in range(2, int(p ** 0.5) + 1)))]
    left_truncatable_primes = []
    for prime in primes:
        digits = [int(d) for d in str(prime)]
        if 0 in digits:
            continue
        is_left_truncatable = True
        for digit in digits:
            digits.pop(0)
            if not all((d % p != 0 for p in range(2, int(digits[0] ** 0.5) + 1) for d in digits)):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort()
    return left_truncatable_primes