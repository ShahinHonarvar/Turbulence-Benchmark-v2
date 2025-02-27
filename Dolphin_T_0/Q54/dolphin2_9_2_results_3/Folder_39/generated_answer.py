def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    else:
        return is_prime(n) and is_right_truncatable(n // 10)

def all_right_truncatable_prime(node):
    x = node[30]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)