import itertools

def all_right_truncatable_prime(x):
    if x[0] == 1:
        return []
    right_truncatable_primes = []
    for p in itertools.prime_number(x[0]):
        if p % 10 in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89):
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes)