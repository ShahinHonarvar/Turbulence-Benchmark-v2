def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[7]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        current = prime
        while current > 1:
            current = current // 10
            if not is_prime(current):
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)