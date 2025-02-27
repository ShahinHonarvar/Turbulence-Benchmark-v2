def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] and int(str(i)[:j]) // 2 > 0 and (int(str(i)[:j]) // 3 > 0) and (int(str(i)[:j]) // 5 > 0) and (int(str(i)[:j]) // 7 > 0) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes)