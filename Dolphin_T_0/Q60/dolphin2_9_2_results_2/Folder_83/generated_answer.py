def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if str(n).count('0') > 0:
        return False
    while len(str(n)) > 1:
        if not is_prime(int(str(n)[1:-1])):
            return False
        n = int(str(n)[1:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[24]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)