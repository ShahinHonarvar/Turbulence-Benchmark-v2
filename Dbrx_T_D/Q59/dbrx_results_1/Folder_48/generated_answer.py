def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_left_truncatable_primes():
    for i in range(1, 10):
        if is_prime(i):
            yield i
    for i in generate_left_truncatable_primes():
        for j in range(10, 100):
            num = i * 10 + j
            if is_prime(num):
                yield num

def all_left_truncatable_prime(n):
    primes = list(generate_left_truncatable_primes())
    return [p for p in primes if p < n]