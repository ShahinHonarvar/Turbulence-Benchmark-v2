def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(t):
    x = t[49]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            if '0' not in s:
                flag = True
                while s and flag:
                    if not is_prime(int(s)):
                        flag = False
                    s = s[1:]
                if flag:
                    primes.append(i)
    primes.sort()
    return primes