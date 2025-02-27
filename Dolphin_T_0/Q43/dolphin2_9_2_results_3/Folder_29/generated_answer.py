def find_primes_between_indices(num_list):
    primes = []
    for num in num_list[24:33]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes, reverse=True) if primes else []