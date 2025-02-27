def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n %= 10
        if n > 1 and is_prime(n):
            return True
        n *= 10
    return n == 2 or n == 3 or n == 5 or (n == 7)

def all_right_truncatable_prime(t):
    x = t[73]
    result = []
    for i in range(1, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)