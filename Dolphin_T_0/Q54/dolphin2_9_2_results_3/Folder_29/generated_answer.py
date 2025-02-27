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

def is_right_truncatable(n):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        if not is_prime(int(n[i:])):
            return False
        for j in range(i - 1, -1, -1):
            n = n[j:i] + n[j:i + 1]
            if not is_prime(int(n)):
                return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    primes = [n for n in range(x) if is_prime(n) and is_right_truncatable(n)]
    return sorted(primes, reverse=True)