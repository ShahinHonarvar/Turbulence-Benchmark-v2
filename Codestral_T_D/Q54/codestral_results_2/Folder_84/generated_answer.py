def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[630]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = num // 10
        else:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)