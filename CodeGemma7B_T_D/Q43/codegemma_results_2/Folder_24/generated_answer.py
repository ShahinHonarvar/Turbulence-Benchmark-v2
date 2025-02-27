def find_primes_between_indices(lst):
    primes = []
    for num in lst[38:56]:
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            primes.append(num)
    primes.sort(reverse=True)
    return primes