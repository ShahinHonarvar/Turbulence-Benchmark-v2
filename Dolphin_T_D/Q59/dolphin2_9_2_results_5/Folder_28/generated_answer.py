def is_left_truncatable_prime(n):
    n = str(n)
    while n and n != '0':
        if not is_prime(int(n)):
            return False
        n = n[1:]
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(a):
    result, x = ([], a[19])
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)