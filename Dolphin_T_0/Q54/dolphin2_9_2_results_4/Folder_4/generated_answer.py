def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    i, w = (3, 2)
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def right_truncatable(n):
    if n < 10:
        return n
    return int(str(n)[-1])

def all_right_truncatable_prime(x):
    primes = []
    for n in range(10, x):
        if is_prime(n):
            while n != right_truncatable(n):
                if not is_prime(n):
                    break
                n = right_truncatable(n)
            else:
                primes.append(int(str(n)))
    return sorted(primes, reverse=True)