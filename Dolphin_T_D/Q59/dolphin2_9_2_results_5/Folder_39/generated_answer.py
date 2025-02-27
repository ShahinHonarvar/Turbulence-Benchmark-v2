def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(x):
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if all((is_prime(int(str(prime)[i:])) for i in range(1, len(str(prime))))):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)

def all_left_truncatable_prime(args):
    return left_truncatable_prime(args[30])