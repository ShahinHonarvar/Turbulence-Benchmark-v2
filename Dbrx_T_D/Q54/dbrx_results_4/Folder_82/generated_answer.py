def is_prime(n):
    if n <= 1:
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

def all_right_truncatable_prime(t):
    x = t[69]
    primes = []
    for i in range(1, x):
        if is_prime(i):
            primes.append(i)
    result = []
    for prime in primes:
        if prime >= x:
            break
        s = str(prime)
        while len(s) > 1:
            if not is_prime(int(s)):
                break
            s = s[:-1]
        if is_prime(int(s)):
            result.append(prime)
    return sorted(result, reverse=True)