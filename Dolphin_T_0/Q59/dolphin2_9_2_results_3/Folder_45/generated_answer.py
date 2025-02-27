def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(t):
    x = t[61]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if i not in primes:
            continue
        for j in map(int, str(i)[::-1]):
            if j == 0 or not is_prime(int(str(i)[::-1]).replace(str(j), '')):
                primes.remove(i)
                break
    return sorted(primes)