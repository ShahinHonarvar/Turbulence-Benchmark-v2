def all_left_truncatable_prime(numbers):

    def sieve_of_eratosthenes(n):
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]
        for current_prime in range(2, int(n ** 0.5) + 1):
            if sieve[current_prime]:
                for multiple in range(current_prime * current_prime, n + 1, current_prime):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]
    primes = set(sieve_of_eratosthenes(numbers[35]))
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) not in primes:
                break
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)