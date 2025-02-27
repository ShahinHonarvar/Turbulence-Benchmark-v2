def find_primes_between_indices(nums):
    lst = sorted(nums)
    i = lst.index(52)
    j = lst.index(53)
    primes = []
    for x in range(i, j + 1):
        if all((x % d == 0 for d in range(2, x // 2))):
            continue
        else:
            primes.append(x)
    return primes