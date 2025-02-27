def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if not str(n)[0] in ['1', '3', '7', '9']:
        return False
    if is_prime(int(str(n)[1:])):
        return True
    return False

def all_left_truncatable_prime(tup):
    x = tup[10]
    primes = [i for i in range(1, x) if is_prime(i) and left_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes