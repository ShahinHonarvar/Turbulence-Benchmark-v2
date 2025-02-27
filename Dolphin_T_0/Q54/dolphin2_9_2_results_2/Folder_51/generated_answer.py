def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(p):
    if len(str(p)) == 1:
        return p
    return int(str(p)[-1]) * 10 ** (len(str(p)) - 1) + right_truncatable(p // 10)

def all_right_truncatable_prime(int_tuple):
    x = int_tuple[54]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_prime(right_truncatable(i)):
            primes.append(i)
    return sorted(primes)