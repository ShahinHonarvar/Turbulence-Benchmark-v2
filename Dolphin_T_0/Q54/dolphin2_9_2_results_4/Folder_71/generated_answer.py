def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = [n for n in range(x - 1, 1, -1) if is_prime(n)]
    right_truncatable = []
    for prime in primes:
        n = prime
        while n > 1:
            n //= 10
            if not is_prime(n):
                right_truncatable = right_truncatable[:-1]
                break
            right_truncatable.append(prime)
    return right_truncatable