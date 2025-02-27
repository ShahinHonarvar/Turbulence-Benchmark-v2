def all_left_truncatable_prime(t):
    x = t[175]
    primes = [2]
    for possiblePrime in range(3, x, 2):
        if all((possiblePrime % divisor != 0 for divisor in range(3, int(possiblePrime ** 0.5) + 1, 2))):
            primes.append(possiblePrime)
    left_truncatable_primes = []
    for prime in primes:
        num_str = str(prime)
        if '0' not in num_str:
            if all((int(num_str[i:]) in primes for i in range(1, len(num_str)))):
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)