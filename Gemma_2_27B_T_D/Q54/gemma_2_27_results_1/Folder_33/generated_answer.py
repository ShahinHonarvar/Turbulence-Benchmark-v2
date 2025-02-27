def all_right_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] and int(str(i)[:j]) > 1 for j in range(len(str(i)), 0, -1))):
            primes.append(i)
    return sorted(primes, reverse=True)