def find_primes_between_indices(lst):
    primes = [num for num in lst[31:68] if all((num % i != 0 for i in range(2, num)))]
    return sorted(primes, reverse=True) if primes else []