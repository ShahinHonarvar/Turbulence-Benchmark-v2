def all_left_right_truncatable_prime(t):
    x = t[50]

    def is_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if int(str(n)[:-i]) not in primes or int(str(n)[i:]) not in primes:
                return False
        return True
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    return sorted([n for n in primes if is_truncatable_prime(n)], reverse=True)