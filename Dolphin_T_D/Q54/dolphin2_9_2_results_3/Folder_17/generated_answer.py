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

def all_right_truncatable_prime(t):
    x = t[36]
    primes = []
    for i in range(x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)