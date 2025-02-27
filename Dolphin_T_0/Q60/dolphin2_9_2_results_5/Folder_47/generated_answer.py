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

def all_left_right_truncatable_prime(t):
    x = t[49]
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            s = str(i)
            if '0' not in s:
                while s:
                    if not is_prime(int(s)):
                        break
                    s = s[1:-1]
                else:
                    primes.append(i)
    return sorted(primes)