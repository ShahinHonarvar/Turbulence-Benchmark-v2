def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    x = t[630]
    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    primes.sort(reverse=True)
    return primes