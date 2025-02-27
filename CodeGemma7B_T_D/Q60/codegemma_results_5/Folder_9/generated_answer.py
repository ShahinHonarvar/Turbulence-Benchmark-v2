from functools import reduce

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

def generate_truncatable_primes(n):
    candidates = list(range(2, n + 1))
    truncatable_primes = []
    while candidates:
        p = candidates.pop()
        if not is_prime(p):
            continue
        str_p = str(p)
        if '0' in str_p:
            continue
        if is_prime(int(str_p[1:])):
            truncatable_primes.append(p)
        for i in range(1, len(str_p) - 1):
            if not is_prime(int(str_p[:i] + str_p[i + 1:])):
                break
            elif i == len(str_p) - 2 and is_prime(int((str_p[i] + str_p[i + 1]) / 2)):
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)

def all_left_right_truncatable_prime(tup):
    x = tup[29]
    return generate_truncatable_primes(x)