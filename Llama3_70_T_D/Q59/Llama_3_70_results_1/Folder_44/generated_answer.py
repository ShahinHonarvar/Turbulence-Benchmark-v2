def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncation(s):
    return [s[i:] for i in range(1, len(s) + 1) if not s[i:].startswith('0')]

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        s = str(prime)
        if '0' not in s and all((is_prime(int(t)) for t in left_truncation(s))):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)