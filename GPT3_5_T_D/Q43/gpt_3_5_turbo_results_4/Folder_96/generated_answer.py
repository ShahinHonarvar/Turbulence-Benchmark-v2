def find_primes_between_indices(lst):
    primes = []
    for num in lst[31:68]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)