def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[18]
    right_truncatable_primes = []

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)