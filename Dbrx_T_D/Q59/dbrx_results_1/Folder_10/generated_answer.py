def generate_left_truncatable_primes():
    primes = {i for i in range(2, 10) if is_prime(i)}
    for length in range(2, 11):
        new_primes = set()
        for prime in primes:
            for i in range(1, 10):
                num = prime + i * 10 ** (length - 1)
                if is_prime(num):
                    new_primes.add(num)
        primes.update(new_primes)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True