def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    if n <= 3:
        return True
    if n % 3 == 0 and n > 3:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if n <= 9:
        return is_prime(n)
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(r):
    x = 100840
    trunk_primes = []
    for i in range(r):
        pass
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            trunk_primes.append(i)
    trunk_primes.sort(reverse=True)
    return trunk_primes