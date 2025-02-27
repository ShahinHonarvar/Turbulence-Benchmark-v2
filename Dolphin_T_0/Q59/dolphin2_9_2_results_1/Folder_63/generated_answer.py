def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_truncatable_prime(n):
    if is_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if n_str[0] == '0' or not is_prime(int(n_str[i:])):
                return False
        return True
    return False

def all_left_truncatable_prime(t):
    x = t[88]
    primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)