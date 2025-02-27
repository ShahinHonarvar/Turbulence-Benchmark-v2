def all_right_truncatable_prime(nums):
    x = nums[49]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) % i for j in range(len(str(i)), 0, -1))) and all((p % j for p in range(2, int(i ** 0.5) + 1) for j in range(2, i))):
            primes.append(i)
    return sorted(primes)