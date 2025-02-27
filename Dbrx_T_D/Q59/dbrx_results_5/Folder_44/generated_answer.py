def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def remove_leading_digit(n):
    s = str(n)
    return int(s[1:]) if len(s) > 1 else 0

def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(1, 10):
        if is_prime(i):
            left_truncatable_primes.append(i)
    for i in range(10, x):
        if is_prime(i) and all((is_prime(remove_leading_digit(j)) for j in left_truncatable_primes)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)