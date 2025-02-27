def find_primes_between_indices(num_list):
    primes = []
    for num in num_list[10:13]:
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            primes.append(num)
    return sorted(primes) if primes else []