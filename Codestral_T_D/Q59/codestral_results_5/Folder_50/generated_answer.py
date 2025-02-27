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

def all_left_truncatable_prime(t):
    x = t[57]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)