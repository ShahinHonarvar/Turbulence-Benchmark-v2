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

def is_left_right_truncatable(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    n = int(str(n)[::-1]) if len(str(n)) > 1 else int(str(n)[0])
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    result = []
    x = t[1]
    for num in range(1, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True) if result else []