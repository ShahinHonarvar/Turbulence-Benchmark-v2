def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        for i in range(len(prime_str), 0, -1):
            if not is_prime(int(prime_str[:i])):
                break
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)