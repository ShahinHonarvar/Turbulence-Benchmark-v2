def all_left_right_truncatable_prime(arg):
    x = arg[97]
    primes = [i for i in range(2, x + 1) if all((i % j for j in range(2, int(i ** 0.5) + 1)))]
    truncatable_primes = []
    for prime in primes:
        if not str(prime).strip('0') or '0' in str(prime):
            continue
        left_truncatable = True
        for i in range(len(str(prime)) - 1):
            if int(str(prime)[:i + 1]) not in primes:
                left_truncatable = False
                break
        right_truncatable = True
        for i in range(len(str(prime)) - 1):
            if int(str(prime)[i + 1:]) not in primes:
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)