def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[92]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    primes.append(i)
    return sorted(primes)