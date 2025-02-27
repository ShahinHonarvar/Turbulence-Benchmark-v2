def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    primes = []
    x = t[992]
    for i in range(2, x):
        if is_prime(i) and is_prime(int(str(i)[:-1])):
            primes.append(i)
    return sorted(primes)