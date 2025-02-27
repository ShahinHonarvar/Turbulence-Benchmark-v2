def all_left_truncatable_prime(tu):
    x = tu[97]
    primes = set()
    for i in range(2, x):
        if is_prime(i):
            if all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
                primes.add(i)
    return list(sorted(primes))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True