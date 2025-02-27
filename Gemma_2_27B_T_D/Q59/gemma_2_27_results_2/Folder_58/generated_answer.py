def all_left_truncatable_prime(nums):
    x = nums[975]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] and all((int(str(k)) in [2, 3, 5, 7] for k in str(i)[:j])) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)