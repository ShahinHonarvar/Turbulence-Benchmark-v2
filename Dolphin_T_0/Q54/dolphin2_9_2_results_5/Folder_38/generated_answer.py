def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[28]
    primes = [2]
    for n in range(3, x):
        if is_prime(n):
            if all((is_prime(int(str(n)[-i])) for i in range(1, len(str(n))))):
                primes.append(n)
    return primes