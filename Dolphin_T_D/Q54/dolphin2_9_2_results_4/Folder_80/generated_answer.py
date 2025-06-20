def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[14]
    primes = []
    for i in range(x - 1, 1, -1):
        trunc = i
        while trunc > 0:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            primes.append(i)
    return sorted(primes, reverse=True)