def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[61]
    primes = []

    def check_right_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    for num in range(2, x):
        if check_right_truncatable(num):
            primes.append(num)
    return primes