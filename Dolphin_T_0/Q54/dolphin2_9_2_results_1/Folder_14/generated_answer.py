import math

def is_prime(n):
    if n == 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(math.sqrt(n)) + 1, 2)))

def all_right_truncatable_prime(args):
    x = args[78]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if all((is_prime(int(str(i)[-k:])) for k in range(1, len(str(i)) + 1))):
                primes.append(i)
    return sorted(primes, reverse=True)