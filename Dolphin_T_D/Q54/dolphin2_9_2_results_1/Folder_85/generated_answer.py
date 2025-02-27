def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[:i])):
                return False
        return is_prime(n)
    x = t[94]
    primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)