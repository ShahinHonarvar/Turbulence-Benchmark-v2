def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[370]
    primes = [i for i in range(x, 0, -1) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if set(str(i)).issubset({'1', '3', '7', '9'}) and all([is_prime(i // 10 ** j) for j in range(1, len(str(i)))])]
    return left_truncatable_primes