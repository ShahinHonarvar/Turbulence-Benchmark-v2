def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[100]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]
    return left_truncatable_primes