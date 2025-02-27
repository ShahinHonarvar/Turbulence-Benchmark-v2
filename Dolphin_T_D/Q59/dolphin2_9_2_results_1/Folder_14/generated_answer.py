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

def truncate_left(n):
    s = str(n)
    while s and is_prime(int(s)):
        s = s[1:]
    return s == ''

def all_left_truncatable_prime(args):
    x = args[78]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    return [i for i in primes if truncate_left(i)]