def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[49]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            trunc = n
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 1:
                    primes.append(n)
    return sorted(primes)