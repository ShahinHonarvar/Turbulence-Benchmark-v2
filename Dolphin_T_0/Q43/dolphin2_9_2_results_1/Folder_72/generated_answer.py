def find_primes_between_indices(lst):
    primes = []
    for num in lst[28:45]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes)