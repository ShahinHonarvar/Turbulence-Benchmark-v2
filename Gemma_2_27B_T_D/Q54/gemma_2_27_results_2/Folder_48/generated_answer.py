def all_right_truncatable_prime(nums):
    x = nums[835]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or all((int(str(i)[:j]) % k for k in range(2, int(int(str(i)[:j]) ** 0.5) + 1))) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes)