def all_right_truncatable_prime(params):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, num):
        if not is_prime(num):
            return False
        while num != 0:
            if not is_prime(num // 10):
                return False
            num //= 10
        return True
    x = params[71]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i, i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True) or []