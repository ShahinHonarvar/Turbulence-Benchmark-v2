def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[31]
    primes = []

    def check_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for i in range(2, x):
        if check_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)