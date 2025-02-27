def find_primes_between_indices(lst):
    list_of_primes = []
    for item in lst:
        if item >= 0 and item <= 1:
            if item != 0:
                list_of_primes.append(item)
    return sorted(list_of_primes)