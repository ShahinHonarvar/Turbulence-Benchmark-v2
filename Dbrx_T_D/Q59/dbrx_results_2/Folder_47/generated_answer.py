import itertools

def generate_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

def is_left_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[1:])
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    primes = generate_primes(max(numbers))
    return [prime for prime in primes if is_left_truncatable_prime(prime) and prime < numbers[49]]