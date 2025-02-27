def find_primes_between_indices(lst):
    prime_lst = []
    for el in lst[33:36]:
        if all((el % i != 0 for i in range(2, el))):
            prime_lst.append(el)
    return sorted(prime_lst)