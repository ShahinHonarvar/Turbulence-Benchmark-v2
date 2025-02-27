def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    current = num
    while current > 0:
        if not is_prime(current):
            return False
        current = int(str(current)[1:]) if len(str(current)) > 1 else 0
    return True

def all_left_truncatable_prime(t):
    x = t[37]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)