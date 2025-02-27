def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[36]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            n = i
            truncatable = True
            while n > 0:
                n //= 10
                if not is_prime(n):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)