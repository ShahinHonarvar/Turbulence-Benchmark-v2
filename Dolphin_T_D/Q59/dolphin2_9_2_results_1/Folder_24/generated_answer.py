def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[65]
    trunc_primes = []
    for num in range(x, 1, -1):
        n = num
        while n:
            if n != num and is_prime(n):
                trunc_primes.append(num)
                break
            n //= 10
    return sorted(trunc_primes, reverse=True)