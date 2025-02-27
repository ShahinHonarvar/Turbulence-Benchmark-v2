def find_primes_between_indices(lst):
    primes = []
    for i in range(24, 84):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag and i not in lst:
            primes.append(i)
    primes.sort()
    return primes