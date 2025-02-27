def find_primes_between_indices(lst):
    primes = []
    for i in lst[19:72]:
        if i > 1:
            n = int(i ** 0.5)
            for j in range(2, n + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return sorted(primes)