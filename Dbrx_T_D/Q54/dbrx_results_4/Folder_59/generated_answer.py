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

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[84]
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
    for i in range(10, x):
        if is_prime(i):
            flag = True
            j = i
            while j > 0:
                if not is_prime(j):
                    flag = False
                    break
                j = remove_last_digit(j)
            if flag:
                primes.append(i)
    return sorted(primes, reverse=True) if primes else []