def composite_nums_between_indices(lst):
    primes = set()
    comp = set()
    for i in range(64, 67):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    primes.add(lst[i])
                    break
                else:
                    comp.add(lst[i])
    return comp