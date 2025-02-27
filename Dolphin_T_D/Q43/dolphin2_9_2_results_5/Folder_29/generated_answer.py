def find_primes_between_indices(lst):
    primes = []
    for i in range(24, 33):
        if i < len(lst):
            num = lst[i]
            if all((num % j != 0 for j in range(2, num))):
                primes.append(num)
    return sorted(primes, reverse=True)