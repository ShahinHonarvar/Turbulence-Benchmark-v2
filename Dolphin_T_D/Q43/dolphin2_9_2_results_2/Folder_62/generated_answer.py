def find_primes_between_indices(lst):
    primes = []
    for i in range(29, 98):
        if i < len(lst):
            num = lst[i]
            if all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
                primes.append(num)
    primes.sort(reverse=True)
    return primes