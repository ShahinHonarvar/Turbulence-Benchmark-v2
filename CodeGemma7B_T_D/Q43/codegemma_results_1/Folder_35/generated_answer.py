def find_primes_between_indices(nums):
    primes = []
    for i in range(112, 362):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    primes.sort(reverse=True)
    return primes