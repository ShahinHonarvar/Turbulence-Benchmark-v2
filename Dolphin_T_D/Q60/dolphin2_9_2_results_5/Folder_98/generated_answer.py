def all_left_right_truncatable_prime(n):
    x = n[8]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def trunc(n):
        return [int(str(n)[i:j]) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)]
    lrt_primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and all((is_prime(j) for j in trunc(i))):
            lrt_primes.append(i)
    return sorted(lrt_primes, reverse=True)