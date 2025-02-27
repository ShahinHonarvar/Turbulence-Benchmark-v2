import itertools

def all_left_truncatable_prime(nums):
    primes = [x for x in nums if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]
    pairs = itertools.accumulate(primes)
    return [x for x in pairs if x[1] in primes and (not any((x[1] % y == 0 for y in range(2, int(x[1] ** 0.5) + 1))))]