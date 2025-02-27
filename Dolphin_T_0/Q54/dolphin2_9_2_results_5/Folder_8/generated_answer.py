def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5)
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[41]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [i for i in primes if i % 10 in primes and int(str(i)[-1]) in primes]
    for _ in range(1, len(str(x))):
        truncatable_primes = [i for i in truncatable_primes if int(str(i)[-2:]) in primes and int(str(i)[-1]) in primes]
    return sorted(truncatable_primes, reverse=True)