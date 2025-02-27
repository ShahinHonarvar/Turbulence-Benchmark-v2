def all_left_truncatable_prime(numbers):
    x = numbers[41]

    def is_left_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if int(str(n)[i:]) not in primes:
                return False
        return True
    primes = set()
    for num in range(2, x):
        if all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes