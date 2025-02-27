import itertools

def all_left_truncatable_prime(test_case):
    primes = set(test_case)
    for p in range(test_case[0], test_case[1] + 1):
        if p in primes:
            yield p
            if p == test_case[0]:
                break
            for prime in itertools.permutations(str(p)):
                if all((int(c) for c in prime)):
                    if int(prime) in primes:
                        yield int(prime)
                        break