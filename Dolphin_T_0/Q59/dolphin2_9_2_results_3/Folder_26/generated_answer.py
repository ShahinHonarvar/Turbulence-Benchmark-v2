def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def is_left_truncatable_prime(n):
    while n:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        if n // 10:
            n //= 10
        else:
            return True
    return True

def all_left_truncatable_prime(intervals):
    x = intervals[81]
    primes = [n for n in range(x, 1, -1) if is_left_truncatable_prime(n)]
    return primes