def find_primes_between_indices(lst):
    nums = lst[19:86]
    primes = [i for i in nums if all((i % j != 0 for j in range(2, i)))]
    return sorted(primes, reverse=True) if primes else []