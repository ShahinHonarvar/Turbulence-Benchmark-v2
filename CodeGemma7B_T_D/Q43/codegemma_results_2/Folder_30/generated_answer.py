def find_primes_between_indices(lst):
    primes = []
    for i in range(61, 81):
        if lst[i] == 2 or (lst[i] % 2 != 0 and lst[i] % 3 != 0 and (lst[i] % 5 != 0) and (lst[i] % 7 != 0)):
            primes.append(lst[i])
    return sorted(primes)[::-1]