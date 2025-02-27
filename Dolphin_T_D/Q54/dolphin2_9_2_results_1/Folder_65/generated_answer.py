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

def all_right_truncatable_prime(t):
    x = t[32]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            trunc = n
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(n)
    primes.sort()
    return primes