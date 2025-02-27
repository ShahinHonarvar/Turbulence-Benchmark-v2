def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = t[433]
    rt_primes = []
    for num in range(x - 1, 1, -1):
        if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            rt_primes.append(num)
    return sorted(rt_primes, reverse=True)