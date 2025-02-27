def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[70]
    primes = [2, 3, 5, 7]
    for i in range(10, x):
        if all(map(lambda x: is_prime(int(str(x))), [i])):
            primes.append(i)
    return [p for p in primes if p < x]