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

def all_left_right_truncatable_prime(t):
    x = t[84]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    left_right_truncatable_primes = []
    for p in primes:
        if '0' not in str(p) and is_prime(int(str(p)[1:-1])) and is_prime(int(str(p)[1:])) and is_prime(int(str(p)[:-1])):
            left_right_truncatable_primes.append(p)
    return left_right_truncatable_primes