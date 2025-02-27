def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[975]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n:
                n //= 10
                if not is_prime(n):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)