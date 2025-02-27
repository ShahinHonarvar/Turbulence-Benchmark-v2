def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[38]
    primes = [p for p in range(2, x + 1) if is_prime(p) and '0' not in str(p)]
    left_right_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        is_left_right_truncatable = True
        while len(prime_str) > 2:
            prime_str = prime_str[1:-1]
            if not is_prime(int(prime_str)):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)