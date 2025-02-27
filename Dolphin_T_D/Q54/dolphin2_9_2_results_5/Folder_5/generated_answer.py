def all_right_truncatable_prime(x):
    primes = []
    for i in range(2, x):
        j = i
        while j != 0 and is_prime(j):
            primes.append(j)
            j = j // 10
    return sorted(primes)

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