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
    x = t[78]
    left_truncatable_primes = []
    for n in range(x, 1, -1):
        s = str(n)
        if '0' in s:
            continue
        if not is_prime(n):
            continue
        for i in range(len(s) - 1):
            if not is_prime(int(s[i:])):
                break
        else:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)