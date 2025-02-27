def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[29]
    primes = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)