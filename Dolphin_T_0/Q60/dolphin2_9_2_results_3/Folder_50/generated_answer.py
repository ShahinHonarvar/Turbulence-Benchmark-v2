def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_and_right_truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        if len(s) > 2 and (not is_prime(int(s[1:-1]))):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[57]
    primes = []
    for i in range(x, 1, -1):
        if is_left_and_right_truncatable(i):
            primes.append(i)
    return primes