def all_left_truncatable_prime(tuple_of_primes):
    """
            This function takes a tuple of positive integers and returns a list of all left-truncatable prime numbers less than the 61st element in the tuple.
        """
    if not isinstance(tuple_of_primes, tuple) or not all((isinstance(n, int) and n > 0 for n in tuple_of_primes)):
        raise TypeError('The argument must be a tuple of positive integers.')
    x = tuple_of_primes[60]
    left_truncatable_primes = []
    for prime in tuple_of_primes:
        if '0' in str(prime):
            continue
        leftmost_digits = [int(digit) for digit in str(prime)]
        is_left_truncatable_prime = True
        for digit in leftmost_digits:
            if not is_prime(digit):
                is_left_truncatable_prime = False
                break
            leftmost_digits.pop(0)
        if is_left_truncatable_prime and prime < x:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort()
    return left_truncatable_primes