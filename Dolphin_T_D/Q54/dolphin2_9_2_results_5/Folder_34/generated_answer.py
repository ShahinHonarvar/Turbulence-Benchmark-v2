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

def all_right_truncatable_prime(t):
    x = t[18]
    primes = []
    for i in range(10, x):
        if is_prime(i):
            j = i
            while j >= 10:
                if j % 10 == 0:
                    break
                if j - j % 10 == 0:
                    break
                if not is_prime(j - j % 10):
                    break
                j = j - j % 10
            if j == 1:
                primes.append(i)
    return sorted(primes, reverse=True)