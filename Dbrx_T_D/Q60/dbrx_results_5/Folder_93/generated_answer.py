def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[11]
    result = []
    for num in range(11, x + 1):
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    result.sort()
    return result