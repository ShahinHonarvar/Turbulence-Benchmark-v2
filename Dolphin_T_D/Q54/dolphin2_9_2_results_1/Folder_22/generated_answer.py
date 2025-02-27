def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[85]
    primes = []
    for i in range(x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(int(str(trunc)[-1:])):
                    break
                trunc = str(trunc)[:-1]
                if len(trunc) == 0:
                    primes.append(i)
    return sorted(primes)