def find_primes_between_indices(lst):
    primes = []
    for num in lst[60:81]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True) if primes else []