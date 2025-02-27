def composite_nums_between_indices(lst):
    primes = set()
    for i in range(40, 201):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    primes.add(lst[i])
                    break
    return primes