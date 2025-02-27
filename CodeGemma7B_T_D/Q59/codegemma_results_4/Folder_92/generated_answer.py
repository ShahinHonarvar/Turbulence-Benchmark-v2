def all_left_truncatable_prime(mytuple):
    """Returns a list of left-truncatable prime numbers less than x."""
    left_truncatable_primes = []
    x = mytuple[7]
    for i in range(2, x):
        if is_prime(i) and (not str(i).startswith('0')):
            digits = list(str(i))
            for j in range(1, len(digits)):
                new_number = int(''.join(digits[j:]))
                if not is_prime(new_number):
                    break
            else:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes