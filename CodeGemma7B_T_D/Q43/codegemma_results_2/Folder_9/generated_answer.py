from math import sqrt

def find_primes_between_indices(lst):
    primes = []
    for num in lst[16:72]:
        if num <= 1:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return sorted(primes)