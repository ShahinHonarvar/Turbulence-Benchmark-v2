def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = []
    for prime in primes:
        if all((is_prime(int(str(prime)[i:])) for i in range(1, len(str(prime))))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)