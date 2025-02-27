def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_rt_prime(n):
    rt = set()
    while n > 0:
        if n not in rt and (not is_prime(n)):
            return False
        rt.add(n)
        n //= 10
    return True

def all_right_truncatable_prime(x):
    return sorted([i for i in range(10, x) if is_prime(i) and is_rt_prime(i)], reverse=True)