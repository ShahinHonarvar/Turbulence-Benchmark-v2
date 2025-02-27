def all_right_truncatable_prime(numbers):
    x = numbers[81]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable_prime = True
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if int(prime_str[:i]) not in primes:
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes