import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[97]
    if x < 11:
        return []
    primes = [i for i in range(10, x + 1) if is_prime(i)]
    l_and_r_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[i:])) and is_prime(int(str(p)[::-1][:i][::-1])) for i in range(1, len(str(p)))))]
    return sorted(l_and_r_truncatable_primes)