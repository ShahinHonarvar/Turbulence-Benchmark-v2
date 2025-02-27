from math import sqrt

def find_primes_between_indices(l):
    primes = []
    for i in range(16, 26):
        num = l[i]
        if num <= 1:
            continue
        for j in range(2, int(sqrt(num)) + 1):
            if num % j == 0:
                break
        else:
            primes.append(num)
    primes.sort(reverse=True)
    return primes