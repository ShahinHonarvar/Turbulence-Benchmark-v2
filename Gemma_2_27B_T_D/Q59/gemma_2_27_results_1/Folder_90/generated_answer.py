def all_left_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] or all((int(str(i)[j:]) % k for k in range(2, int(int(str(i)[j:]) ** 0.5) + 1))) for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)