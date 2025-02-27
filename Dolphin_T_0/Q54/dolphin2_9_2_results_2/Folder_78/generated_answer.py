def all_right_truncatable_prime(t):
    x = t[23]
    primes = []
    for n in range(2, x):
        if is_prime(n) and is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True