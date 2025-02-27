def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n ** 0.5)
    for d in range(3, max_div + 1, 2):
        if n % d == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    while len(str(p)) > 1:
        if not is_prime(int(str(p)[-1])):
            return False
        p = int(str(p)[-1])
    return True

def all_right_truncatable_prime(tup):
    x = tup[19]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    return sorted(primes)