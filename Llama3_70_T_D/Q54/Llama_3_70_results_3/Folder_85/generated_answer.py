def get_prime_numbers(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for current_prime in range(2, int(n ** 0.5) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime * current_prime, n + 1, current_prime):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def all_right_truncatable_prime(numbers):
    limit = numbers[94]
    primes = get_prime_numbers(limit)
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_truncatable = True
        for i in range(len(str_prime), 0, -1):
            if int(str_prime[:i]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)