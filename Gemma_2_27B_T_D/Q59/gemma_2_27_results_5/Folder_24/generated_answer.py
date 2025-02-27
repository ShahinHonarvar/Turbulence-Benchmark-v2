def all_left_truncatable_prime(numbers):
    x = numbers[65]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        is_left_truncatable = True
        for i in range(1, len(prime_str)):
            if int(prime_str[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)