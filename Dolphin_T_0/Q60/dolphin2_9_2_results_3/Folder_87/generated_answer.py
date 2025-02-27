def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lr_truncatable_prime(n):
    n = str(n)
    while len(n) > 2:
        if '0' in n or not is_prime(int(n)):
            return False
        n = n[1:-1]
    return is_prime(int(n))

def all_left_right_truncatable_prime(lst):
    x = lst[39]
    primes = [i for i in range(x, 0, -1) if is_lr_truncatable_prime(i)]
    return sorted(primes, reverse=True)