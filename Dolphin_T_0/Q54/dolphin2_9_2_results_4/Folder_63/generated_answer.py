def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_rtrunc_prime(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_right_truncatable_prime(a):
    x = a[88]
    primes = []
    for i in range(x):
        if is_rtrunc_prime(i):
            primes.append(i)
    return sorted(primes)