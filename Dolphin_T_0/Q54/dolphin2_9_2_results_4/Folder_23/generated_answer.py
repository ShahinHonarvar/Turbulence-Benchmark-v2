def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def right_truncatable_prime(n):
    if is_prime(n):
        return True
    else:
        return False

def all_right_truncatable_prime(t):
    x = t[77]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)