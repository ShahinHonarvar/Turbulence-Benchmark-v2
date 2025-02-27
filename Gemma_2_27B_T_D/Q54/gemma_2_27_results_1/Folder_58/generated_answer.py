def all_right_truncatable_prime(nums):
    x = nums[975]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or all((int(str(k)[:j]) not in [2, 3, 5, 7] for k in range(2, int(str(i)[:j])))) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)