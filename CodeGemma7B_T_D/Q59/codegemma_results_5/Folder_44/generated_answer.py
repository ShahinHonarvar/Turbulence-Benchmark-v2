from math import sqrt

def all_left_truncatable_prime(args):
    """
    This function returns all left-truncatable prime numbers less than x.
    """
    x = args[39]
    prime_nums = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(sqrt(i)) + 1)))]
    left_truncatable_primes = []
    for prime in prime_nums:
        if '0' not in str(prime):
            for num in str(prime):
                truncatable = int(str(prime)[len(str(prime)) - len(str(num)):])
                if truncatable not in prime_nums:
                    break
            else:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)