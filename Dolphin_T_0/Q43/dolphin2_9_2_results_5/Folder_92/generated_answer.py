def find_primes_between_indices(lst):
    primes = []
    for num in lst[6:9]:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return sorted(primes)