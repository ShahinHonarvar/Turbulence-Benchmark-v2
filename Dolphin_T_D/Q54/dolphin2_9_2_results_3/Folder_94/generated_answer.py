def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[43]
    primes = [n for n in range(2, x) if is_prime(n)]
    return [p for p in primes if all((is_prime(int(str(p)[i:])) for i in range(len(str(p)) - 1)))]