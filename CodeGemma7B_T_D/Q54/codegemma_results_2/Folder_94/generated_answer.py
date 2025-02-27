def all_right_truncatable_prime(t):
    x = t[43]

    def right_truncatable_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        return all((n % d for d in range(5, int(n ** 0.5) + 1, 6)))

    def prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def right_truncatable_primes(l):
        return [n for n in l if right_truncatable_prime(n)]
    ans = right_truncatable_primes(filter(prime, range(2, x)))
    return sorted(ans) if ans else []