def all_left_truncatable_prime(t):
    x = t[38]
    primes = [2, 3, 5, 7]
    for m in range(10, x):
        if is_prime(m) and is_truncat_left(m, primes):
            primes.append(m)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n and n % i != 0:
        i += 2
    return i * i > n

def is_truncat_left(m, primes):
    if m < 10:
        return True
    else:
        new_m = m // 10
        if new_m in primes and m % 10 != 0:
            return is_truncat_left(new_m, primes)
        else:
            return False