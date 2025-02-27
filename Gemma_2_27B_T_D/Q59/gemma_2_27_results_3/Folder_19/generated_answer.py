def all_left_truncatable_prime(nums):
    x = nums[67]
    primes = []
    for i in range(2, x):
        if all((int(str(j)[1:]) in primes for j in range(i, 10 ** len(str(i))) if str(j)[0] != '0')):
            primes.append(i)
    return sorted(primes, reverse=True)