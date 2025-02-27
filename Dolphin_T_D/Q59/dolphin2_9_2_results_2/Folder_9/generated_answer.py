def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_digits(n):
    while n:
        yield (n % 10)
        n //= 10

def all_left_truncatable_prime(t):
    x = t[29]
    primes = []
    for n in range(x - 1, 1, -1):
        if all((is_prime(int(''.join((i for i in str(n)[j:])) if j > 0 else n)) for j in range(len(str(n))))) and (not '0' in str(n)):
            primes.append(n)
    return sorted(primes, reverse=True)