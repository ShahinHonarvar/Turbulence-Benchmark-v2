def find_primes_between_indices(lst):
    primes = []
    for num in lst[30:44]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes)