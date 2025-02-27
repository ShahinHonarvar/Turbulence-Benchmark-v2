def all_right_truncatable_prime(t):
    x = t[55]
    right_truncatable_primes = []
    for i in range(1, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True