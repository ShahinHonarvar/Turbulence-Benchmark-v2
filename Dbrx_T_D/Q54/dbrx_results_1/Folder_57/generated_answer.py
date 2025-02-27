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

def is_right_truncatable_prime(num):
    while num > 0:
        if num not in primes:
            return False
        num = int(str(num)[1:])
    return True

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for prime in primes:
        if prime >= x:
            break
        if is_right_truncatable_prime(prime):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)