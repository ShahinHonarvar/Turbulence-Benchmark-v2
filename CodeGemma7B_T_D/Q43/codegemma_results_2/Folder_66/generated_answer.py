def find_primes_between_indices(lst):
    primes = []
    for i in range(72, 73):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            continue
        for j in range(5, int(i ** 0.5) + 1, 6):
            if i % j == 0 or i % (j + 2) == 0:
                break
        else:
            primes.append(i)
    return primes