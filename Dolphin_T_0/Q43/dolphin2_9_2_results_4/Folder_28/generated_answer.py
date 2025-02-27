def find_primes_between_indices(lst):
    primes = []
    for num in lst[38:55]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes, reverse=True) if primes else []