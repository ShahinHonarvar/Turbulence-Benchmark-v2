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

def all_left_truncatable_prime(t):
    x = t[41]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            s = str(n)
            while s != '':
                if is_prime(int(s)):
                    s = s[1:]
                else:
                    break
            else:
                primes.append(n)
    return sorted(primes)