def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[4]
    right_truncatable_primes = []
    for possiblePrime in range(2, x):
        if is_prime(possiblePrime):
            prime_str = str(possiblePrime)
            is_right_truncatable = True
            for i in range(len(prime_str) - 1, 0, -1):
                truncated_str = prime_str[:i]
                if not is_prime(int(truncated_str)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(possiblePrime)
    return sorted(right_truncatable_primes)