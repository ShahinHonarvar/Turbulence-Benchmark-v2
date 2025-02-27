def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[992]
    primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        for p in primes:
            if str(p) in str(i):
                break
        else:
            if is_prime(i):
                primes.append(i)
    return primes