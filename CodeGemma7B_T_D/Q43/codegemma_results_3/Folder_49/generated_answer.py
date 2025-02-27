def find_primes_between_indices(lst):
    lst_prime = [num for num in lst[22:51] if num % num == 0]
    lst_prime = sorted(lst_prime, reverse=True)
    return lst_prime if lst_prime else []