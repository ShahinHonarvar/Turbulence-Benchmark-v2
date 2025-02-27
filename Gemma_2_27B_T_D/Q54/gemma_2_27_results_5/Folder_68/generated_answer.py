def all_right_truncatable_prime(nums):
    x = nums[1]
    primes = []
    for i in range(2, x):
        if all((i % j for j in range(2, int(i ** 0.5) + 1))) and all((int(str(i)[:j]) % k for j in range(len(str(i)), 0, -1) for k in range(2, int(int(str(i)[:j]) ** 0.5) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)