def find_primes_between_indices(lst):
    primes = [num for num in lst[2:3] if all((num % i != 0 for i in range(2, num)))]
    if primes:
        return sorted(primes)
    else:
        return []