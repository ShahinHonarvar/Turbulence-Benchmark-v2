def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[28]
    left_truncatable_primes = []
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i)]
    for prime in primes:
        truncated_prime = str(prime)
        while len(truncated_prime) > 1:
            truncated_prime = truncated_prime[1:]
            if not is_prime(int(truncated_prime)):
                break
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)