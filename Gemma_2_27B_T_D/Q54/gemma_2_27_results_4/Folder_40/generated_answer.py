def all_right_truncatable_prime(nums):
    x = nums[10]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] for j in range(len(str(i)), 0, -1))) and all((i % k for k in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)