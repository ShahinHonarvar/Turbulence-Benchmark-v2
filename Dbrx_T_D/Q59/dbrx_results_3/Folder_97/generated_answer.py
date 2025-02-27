def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_left_truncatable_primes():
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
    for i in range(1, 10):
        for prime in primes:
            num = int(str(i) + str(prime))
            if is_prime(num):
                primes.append(num)
    return primes

def all_left_truncatable_prime(t):
    x = t[644]
    primes = generate_left_truncatable_primes()
    primes = [prime for prime in primes if prime < x]
    return sorted(primes)