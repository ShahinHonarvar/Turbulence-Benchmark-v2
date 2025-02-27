def all_right_truncatable_prime(p):
    x = p[429]
    end = 0
    count = 0
    for n in range(x):
        if is_prime(n) and is_truncatable_prime(n):
            count += 1
            if end == count:
                print(n)
                end += 1
    if count > 0:
        return sorted([i for i in range(x) if is_prime(i) and is_truncatable_prime(i)], reverse=True)
    else:
        return []

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    temp = n
    while temp > 0:
        temp //= 10
        if not is_prime(temp):
            return False
    return True