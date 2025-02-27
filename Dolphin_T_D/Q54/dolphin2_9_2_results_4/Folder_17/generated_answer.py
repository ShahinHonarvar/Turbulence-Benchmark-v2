def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[36]
    primes = [i for i in reversed(range(2, x)) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        if all((is_prime(int(str(prime)[-j:])) for j in range(1, len(str(prime))))):
            right_truncatable_primes.append(prime)
    return right_truncatable_primes