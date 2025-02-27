def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[19]
    primes = [2, 3, 5, 7]
    for n in range(10, x):
        if is_prime(n) and all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))):
            primes.append(n)
    return sorted(primes)