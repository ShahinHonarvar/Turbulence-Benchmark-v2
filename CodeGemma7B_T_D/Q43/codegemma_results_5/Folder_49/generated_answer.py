def find_primes_between_indices(lst):
    primal = [num for num in lst[22:51] if all((num % i != 0 for i in range(2, num)))]
    return sorted(primal, reverse=True) or []