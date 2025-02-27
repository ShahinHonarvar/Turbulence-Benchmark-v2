def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(t):
    x = t[97]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            m = n
            while m > 1:
                m //= 10
                if not is_prime(m):
                    break
                if m == 1:
                    primes.append(n)
    return sorted(primes, reverse=True)