from math import sqrt

def find_primes_between_indices(lst):
    primes = []
    for num in lst[23:40]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)