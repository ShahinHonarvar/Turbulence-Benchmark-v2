def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(n):
    while n > 0 and is_prime(n):
        yield n
        n //= 10

def all_right_truncatable_prime(t):
    x = t[14]
    result = []
    for i in range(1, 10):
        for p in right_truncatable_prime(i):
            if p < x:
                result.append(p)
    if not result:
        return []
    return sorted(result, reverse=True)