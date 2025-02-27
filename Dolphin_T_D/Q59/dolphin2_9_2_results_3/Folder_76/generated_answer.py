def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[370]
    primes = [i for i in range(x) if is_prime(i)]
    left_truncatables = [i for i in primes if i % 10 != 0 and int(str(i)[1:]) in primes]
    return sorted(left_truncatables, reverse=True)