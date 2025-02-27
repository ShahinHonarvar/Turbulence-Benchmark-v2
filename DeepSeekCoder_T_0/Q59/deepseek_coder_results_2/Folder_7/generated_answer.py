def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []

    def generate(n):
        if n >= limit or not is_prime(n):
            return
        primes.append(n)
        for i in range(1, 10):
            generate(n * 10 + i)
    for i in range(1, 10):
        generate(i)
    return sorted(primes)

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    return left_truncatable_primes(x)