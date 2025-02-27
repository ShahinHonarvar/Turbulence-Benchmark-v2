from itertools import islice

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
        i += 2
    return True

def is_left_truncatable_prime(n):
    return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:-i])) for i in range(1, len(str(n)))))

def all_left_right_truncatable_prime(t):
    x = t[7]
    primes = [i for i in range(2, x + 1) if is_left_truncatable_prime(i) and is_right_truncatable_prime(i)]
    return sorted(primes)