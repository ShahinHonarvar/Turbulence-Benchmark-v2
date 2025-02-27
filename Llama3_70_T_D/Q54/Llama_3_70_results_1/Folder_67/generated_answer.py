def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    truncatable_primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in truncatable_primes:
        prime_str = str(prime)
        is_right_truncatable = True
        for i in range(len(prime_str)):
            if not is_prime(int(prime_str[:-i - 1])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)