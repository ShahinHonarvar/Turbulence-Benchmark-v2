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

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 1:
        n /= 10
        if not is_prime(int(n)) or n < 10:
            return False
    return True

def all_left_right_truncatable_prime(n):
    if n < 10 > 7:
        return []
    result = []
    for i in range(10, n + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)