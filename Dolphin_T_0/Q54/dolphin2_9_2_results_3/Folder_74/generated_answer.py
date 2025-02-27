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

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in range(len(str(n)), -1, -1):
        if not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_right_truncatable_prime(n_tuple):
    x = n_tuple[36]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes)