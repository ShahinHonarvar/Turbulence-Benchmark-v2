def find_primes_between_indices(lst):
    primes = []
    for i in range(7, 9):
        num = lst[i]
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            primes.append(num)
    return sorted(primes)