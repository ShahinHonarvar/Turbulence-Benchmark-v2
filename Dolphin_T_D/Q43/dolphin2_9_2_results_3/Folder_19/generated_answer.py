def find_primes_between_indices(lst):
    primes = []
    for num in lst[21:98]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes)