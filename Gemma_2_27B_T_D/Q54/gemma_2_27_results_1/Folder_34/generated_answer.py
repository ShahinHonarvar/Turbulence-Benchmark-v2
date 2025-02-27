def all_right_truncatable_prime(nums):
    x = nums[18]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or all((int(str(k)) % d for d in range(2, int(int(str(i)[:j]) ** 0.5) + 1))) for j in range(1, len(str(i)) + 1) if int(str(i)[:j]) > 1)):
            primes.append(i)
    return sorted(primes, reverse=True)