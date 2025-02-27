def all_left_truncatable_prime(tupl):
    """
    This function takes an argument which is a tuple of positive integers. The integer at position 38 will be referred to as x. The function returns the list of all left-truncatable prime numbers less than x. The return list should be sorted in descending order.
    A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
    """
    x = tupl[38]
    results = []
    primes = prime_sieve(x)
    for prime in primes:
        if '0' not in str(prime):
            is_truncatable = True
            for i in range(1, len(str(prime))):
                number = int(str(prime)[i:])
                if number not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                results.append(prime)
    return sorted(results, reverse=True)

def prime_sieve(x):
    """
    This function generates a list of primes up to x.
    """
    primes = []
    for i in range(2, x + 1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes