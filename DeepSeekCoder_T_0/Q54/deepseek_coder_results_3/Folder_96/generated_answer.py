def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[29]
    right_truncatable_primes = []

    def check_right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for i in range(2, x):
        if check_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)