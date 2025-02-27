def all_left_right_truncatable_prime(tup):
    num = tup[41]
    primes = [i for i in range(2, num + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            for i in range(1, len(str_prime)):
                left_prime = int(str_prime[:i])
                right_prime = int(str_prime[i:])
                if is_prime(left_prime) and is_prime(right_prime):
                    left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)