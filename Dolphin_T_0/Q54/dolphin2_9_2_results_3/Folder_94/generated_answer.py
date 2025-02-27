def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[43]
    primes = []
    for i in range(2, x - 1):
        if is_prime(i):
            trunc = i
            while trunc:
                if is_prime(trunc):
                    trunc //= 10
                else:
                    break
            else:
                primes.append(i)
    return sorted(primes)