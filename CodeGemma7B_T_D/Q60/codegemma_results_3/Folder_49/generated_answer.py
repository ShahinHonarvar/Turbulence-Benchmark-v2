def isprime(n):
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

def islefttruncatableprime(n):
    s = str(n)
    if '0' in s:
        return False
    for k in range(1, len(s)):
        if not isprime(int(s[k:])):
            return False
    return True

def isrighttruncatableprime(n):
    s = str(n)
    if '0' in s:
        return False
    for k in range(len(s) - 2, -1, -1):
        if not isprime(int(s[k:])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    return sorted([k for k in range(2, x + 1) if islefttruncatableprime(k) and isrighttruncatableprime(k)])