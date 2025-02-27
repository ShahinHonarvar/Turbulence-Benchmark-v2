def find_primes_between_indices(lst):
    is_prime = lambda num: all((num % i != 0 for i in range(2, num)))
    return sorted([num for num in lst[10:13] if is_prime(num)])