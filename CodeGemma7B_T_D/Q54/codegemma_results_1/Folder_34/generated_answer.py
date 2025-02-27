from itertools import permutations

def all_right_truncatable_prime(t):
    x = t[18]
    primes = [i for i in range(2, x) if 1 not in [i % j for j in range(2, int(i ** 0.5) + 1)]]
    right_trunc = []
    for p in primes:
        if all([int(''.join(map(str, perm))) in primes for perm in permutations(str(p))[:-1]]):
            right_trunc.append(p)
    return sorted(right_trunc, reverse=True)