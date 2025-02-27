def all_right_truncatable_prime(nums):
    x = nums[3]
    primes = []
    for p in range(2, x):
        if all((int(str(p)[:i]) in primes for i in range(1, len(str(p))))):
            primes.append(p)
    return sorted(primes, reverse=True)